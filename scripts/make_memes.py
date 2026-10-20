#!/usr/bin/env python3
"""
Imgflip meme generator for the blog.

General purpose CLI. Point it at a template and some text and it writes the image into
static/images/memes/.

Credentials come from the environment or a gitignored .env file next to this
script.

Setup:
    export IMGF_API_KEY='...'        # create one at https://imgflip.com/api-settings
    # or: export IMGF_USERNAME='...' IMGF_PASSWORD='...'

Usage:
    # browse templates
    ./scripts/make_memes.py templates
    ./scripts/make_memes.py templates --search "drake"

    # two-line meme
    ./scripts/make_memes.py make -t 61579 -p "one does not simply" -b "guess ohm's law" -o ohm

    # any number of text boxes, custom colours and positions
    ./scripts/make_memes.py make -t 93895088 -o expanding \
        --boxes '[{"text":"a"},{"text":"b"},{"text":"c"},{"text":"d"}]'

    # batch from a JSON file
    ./scripts/make_memes.py batch memes.json
    ./scripts/make_memes.py batch memes.json --dry-run

For "boxes" text you can also use the shorthand fields, which map straight onto
the imgflip form parameters:
    {"name":"x","template_id":"61579","text0":"top","text1":"bottom"}

Watermarks: free-tier output carries an imgflip.com watermark. Passing
--no-watermark needs an account with Imgflip Premium.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API_CAPTION = "https://api.imgflip.com/caption_image"
API_GET_MEMES = "https://api.imgflip.com/get_memes"
API_SEARCH_MEMES = "https://api.imgflip.com/search_memes"

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT_DIR = REPO_ROOT / "static" / "images" / "memes"
ENV_FILE = REPO_ROOT / ".env"
USER_AGENT = "hexrogue-meme-gen/1.0"

# Templates that show people, kept out by default. Enable with --allow-people.
# Edit freely, this is just a starting list.
PEOPLE_TEMPLATES = {
    "112126428": "Distracted Boyfriend",
    "224015000": "Bernie Sanders",
    "224514655": "Anime Girl Hiding from Terminator",
    "26036802": "Overly Attached Girlfriend",
    "217743513": "UNO Draw 25 (group)",
    "180190441": "They're The Same Picture",
    "188390779": "Woman Yelling At Cat",
    "252758727": "Mother Ignoring Kid Drowning In A Pool",
    "97984": "Disaster Girl",
    "101288": "Third World Skeptical Kid",
    "226297822": "Panik Kalm Panik",
    "247375501": "Buff Doge vs Cheems",
}


class MemeError(Exception):
    """A user-facing failure with an actionable message."""


def load_dotenv(path: Path = ENV_FILE) -> None:
    """Populate os.environ from a simple KEY=value file, no dependencies."""
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def require_credentials() -> None:
    load_dotenv()
    if os.environ.get("IMGF_API_KEY"):
        return
    if os.environ.get("IMGF_USERNAME") and os.environ.get("IMGF_PASSWORD"):
        return
    raise MemeError(
        "no credentials found.\n"
        "  Preferred: export IMGF_API_KEY='...' (create one at https://imgflip.com/api-settings)\n"
        "  Legacy:     export IMGF_USERNAME='...' IMGF_PASSWORD='...'\n"
        "  Or put either in a .env file, which is gitignored."
    )


def auth_fields() -> dict[str, str]:
    """Legacy form auth, used only when no API key is present."""
    username = os.environ.get("IMGF_USERNAME")
    password = os.environ.get("IMGF_PASSWORD")
    if not (username and password):
        return {}
    # A password copied out of a URL may still be percent-encoded.
    return {"username": username, "password": urllib.parse.unquote(password)}


def request_json(url: str, data: bytes | None = None) -> dict:
    headers = {"User-Agent": USER_AGENT}
    api_key = os.environ.get("IMGF_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        try:
            body = json.loads(raw or "{}")
        except json.JSONDecodeError:
            body = {"error_message": raw[:200]}
        body.setdefault("error_message", f"HTTP {exc.code}")
        body["_http_status"] = exc.code
        return body
    except urllib.error.URLError as exc:
        raise MemeError(f"network error talking to imgflip: {exc.reason}") from exc


def caption_image(fields: dict[str, str]) -> dict:
    """POST to /caption_image. Returns the response with data flattened."""
    body = request_json(API_CAPTION, urllib.parse.urlencode(fields).encode())
    if body.get("success") and isinstance(body.get("data"), dict):
        return {**body["data"], "success": True}
    if body.get("success"):
        return body
    raise MemeError(body.get("error_message") or "imgflip returned an unknown error")


def download(url: str, target: Path) -> None:
    """Fetch the image. i.imgflip.com 403s the default urllib User-Agent."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=120) as response:
        target.write_bytes(response.read())


def slugify(text: str) -> str:
    keep = [c.lower() if c.isalnum() else "-" for c in text]
    slug = "".join(keep)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")[:60] or "meme"


def check_people(template_id: str, allow_people: bool) -> None:
    name = PEOPLE_TEMPLATES.get(str(template_id))
    if name and not allow_people:
        raise MemeError(
            f"template {template_id} ({name}) shows people. "
            f"Pass --allow-people if you want it anyway."
        )


def build_fields(
    template_id: str,
    boxes: list[dict] | None,
    text_fields: dict[str, str],
    font: str | None,
    max_font_size: int | None,
    no_watermark: bool,
) -> dict[str, str]:
    fields = {"template_id": str(template_id)}
    if boxes is not None:
        for index, box in enumerate(boxes):
            if "text" not in box:
                raise MemeError(f"box {index} is missing a 'text' value")
            for key, value in box.items():
                fields[f"boxes[{index}][{key}]"] = str(value)
    else:
        for index in range(20):
            key = f"text{index}"
            if key not in text_fields:
                break
            fields[key] = text_fields[key]
    if font:
        fields["font"] = font
    if max_font_size:
        fields["max_font_size"] = str(max_font_size)
    if no_watermark or os.environ.get("NO_WATERMARK") == "1":
        fields["no_watermark"] = "1"
    fields.update(auth_fields())
    return fields


def resolve_out_path(name: str | None, top_text: str | None, out_dir: Path) -> Path:
    """Work out the destination filename: explicit name, else derived from text."""
    if name:
        stem = slugify(name)
    elif top_text:
        stem = "meme-" + slugify(top_text)
    else:
        raise MemeError("need a name: pass --name or some top text to derive one from")
    if not stem.startswith("meme-"):
        stem = "meme-" + stem
    return out_dir / f"{stem}.jpg"


def render(
    fields: dict[str, str],
    target: Path,
    dry_run: bool,
    quiet: bool = False,
) -> str | None:
    """Create the meme and save it. Returns the imgflip page URL."""
    if not target.parent.is_dir():
        if dry_run:
            return None
        target.parent.mkdir(parents=True, exist_ok=True)

    result = caption_image(fields)
    url = result["url"]
    page = result.get("page_url", "")

    if not dry_run:
        download(url, target)

    if not quiet:
        verb = "would create" if dry_run else "wrote"
        print(f"{verb}: {target}")
        if page:
            print(f"        {page}")
    return page or None


def split_top(texts: list[str], top: str | None) -> tuple[dict[str, str], list[dict] | None]:
    """Turn CLI text input into either textN fields or a boxes array."""
    if not texts:
        return {}, None
    return {}, [{"text": t} for t in texts]


def cmd_templates(args: argparse.Namespace) -> int:
    query = (args.search or "").strip()
    if query:
        payload = urllib.parse.urlencode({"query": query}).encode()
        body = request_json(API_SEARCH_MEMES, payload)
        memes = (body.get("data") or {}).get("memes", [])
        if body.get("_http_status") == 402:
            raise MemeError(
                "template search needs Imgflip Premium. "
                "Drop --search and browse the free top-100 list instead."
            )
    else:
        body = request_json(API_GET_MEMES)
        memes = (body.get("data") or {}).get("memes", [])

    for meme in memes:
        flag = " " + PEOPLE_TEMPLATES.get(str(meme["id"]), "") if args.people else ""
        print(f"{meme['id']:>12}  {meme['width']}x{meme['height']:<6} "
              f"boxes:{meme['box_count']}  {meme['name']}{flag}")

    if not args.people:
        print("\n(Pass --people to also show templates with people in them.)")
    return 0


def cmd_make(args: argparse.Namespace) -> int:
    require_credentials()
    check_people(args.template, args.allow_people)

    if args.boxes:
        try:
            boxes = json.loads(args.boxes)
        except json.JSONDecodeError as exc:
            raise MemeError(f"--boxes is not valid JSON: {exc}") from exc
        if not isinstance(boxes, list) or not boxes:
            raise MemeError("--boxes must be a non-empty JSON array of objects")
        text_fields: dict[str, str] = {}
    else:
        boxes = None
        texts = [t for t in (args.text or []) if t]
        if args.top or args.bottom:
            texts = [t for t in (args.top, args.bottom) if t is not None] + texts
        if not texts:
            raise MemeError("give me something to write: --top/--bottom, --text, or --boxes")
        text_fields = {f"text{i}": t for i, t in enumerate(texts)}

    fields = build_fields(
        args.template, boxes, text_fields, args.font, args.max_font_size, args.no_watermark
    )
    target = resolve_out_path(args.name, args.top, Path(args.out_dir))
    render(fields, target, args.dry_run)
    return 0


def cmd_batch(args: argparse.Namespace) -> int:
    require_credentials()
    path = Path(args.file)
    if not path.is_file():
        raise MemeError(f"no such file: {path}")

    try:
        entries = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise MemeError(f"{path} is not valid JSON: {exc}") from exc

    if not isinstance(entries, list) or not entries:
        raise MemeError(f"{path} must contain a non-empty JSON array")

    out_dir = Path(args.out_dir)
    failures = 0

    for index, entry in enumerate(entries):
        label = entry.get("name") or f"entry {index}"
        try:
            if not entry.get("template_id"):
                raise MemeError("missing template_id")
            check_people(entry["template_id"], args.allow_people)

            boxes = entry.get("boxes")
            text_fields = {
                key: value
                for key, value in entry.items()
                if key.startswith("text") and isinstance(value, str)
            }

            fields = build_fields(
                entry["template_id"],
                boxes,
                text_fields,
                entry.get("font", args.font),
                entry.get("max_font_size", args.max_font_size),
                entry.get("no_watermark", args.no_watermark),
            )
            target = resolve_out_path(label, None, out_dir)
            render(fields, target, args.dry_run, quiet=args.quiet)
            if not args.dry_run and not args.quiet:
                time.sleep(args.delay)
        except MemeError as exc:
            failures += 1
            print(f"FAIL {label}: {exc}", file=sys.stderr)

    if failures:
        print(f"\n{failures} of {len(entries)} failed.", file=sys.stderr)
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="make_memes.py",
        description="Generate blog memes with the imgflip API.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    common_out = argparse.ArgumentParser(add_help=False)
    common_out.add_argument(
        "-o", "--out-dir", default=str(DEFAULT_OUT_DIR),
        help=f"output directory (default: {DEFAULT_OUT_DIR})",
    )
    common_out.add_argument("--dry-run", action="store_true", help="talk to the API, save nothing")
    common_out.add_argument(
        "--allow-people", action="store_true",
        help="permit templates that show people (blocked by default)",
    )

    p_templates = sub.add_parser("templates", help="list meme templates")
    p_templates.add_argument("-s", "--search", help="search templates (needs Premium)")
    p_templates.add_argument("--people", action="store_true", help="include people templates")
    p_templates.set_defaults(func=cmd_templates)

    p_make = sub.add_parser("make", parents=[common_out], help="create a single meme")
    p_make.add_argument("-t", "--template", required=True, help="imgflip template id")
    p_make.add_argument("-n", "--name", help="output name, e.g. ohm-law")
    p_make.add_argument("-p", "--top", help="top text")
    p_make.add_argument("-b", "--bottom", help="bottom text")
    p_make.add_argument(
        "--text", action="append",
        help="extra text box, repeatable. Order: top, bottom, then these",
    )
    p_make.add_argument("--boxes", help="full JSON boxes array, overrides --top/--bottom")
    p_make.add_argument("--font", help="font family, e.g. impact, arial, or a Google Font name")
    p_make.add_argument("--max-font-size", type=int, help="max font size in pixels")
    p_make.add_argument("--no-watermark", action="store_true", help="needs Imgflip Premium")
    p_make.set_defaults(func=cmd_make)

    p_batch = sub.add_parser("batch", parents=[common_out], help="create many from a JSON file")
    p_batch.add_argument("file", help="path to the JSON array")
    p_batch.add_argument("--font", help="default font for entries without one")
    p_batch.add_argument("--max-font-size", type=int, help="default max font size")
    p_batch.add_argument("--no-watermark", action="store_true", help="needs Imgflip Premium")
    p_batch.add_argument("--delay", type=float, default=0.5, help="seconds between requests")
    p_batch.add_argument("--quiet", action="store_true", help="only print failures")
    p_batch.set_defaults(func=cmd_batch)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except MemeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
