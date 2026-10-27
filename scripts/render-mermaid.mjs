#!/usr/bin/env node
// Pre-render every ```mermaid fence in content/ to an SVG in static/images/diagrams/.
// Run before `hugo`. The matching Hugo hook is
// layouts/_default/_markup/render-codeblock-mermaid.html, which builds the same
// /images/diagrams/mermaid-<hash>.svg path from the hash of the fence body.
//
// Needs a Chrome build. Set PUPPETEER_EXECUTABLE_PATH, or install one with:
//   npx @puppeteer/browsers install chrome@stable --path .cache/browsers
// mmdc must be on PATH, or point MMDC at it:
//   npm install -g @mermaid-js/mermaid-cli
//
//   node scripts/render-mermaid.mjs          # render what changed
//   node scripts/render-mermaid.mjs --force  # re-render everything
//
// shortcut: the hash covers the fence body only, so a theme change in
// scripts/mermaid-theme.json needs one run with --force.
import { createHash } from 'node:crypto'
import { execFileSync } from 'node:child_process'
import {
  mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, statSync, writeFileSync,
} from 'node:fs'
import { tmpdir } from 'node:os'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = join(dirname(fileURLToPath(import.meta.url)), '..')
const outDir = join(root, 'static', 'images', 'diagrams')
const theme = join(root, 'scripts', 'mermaid-theme.json')
const puppeteer = join(root, 'scripts', 'mermaid-puppeteer.json')
const mmdc = process.env.MMDC || 'mmdc'
const force = process.argv.includes('--force')

const FENCE = /^[ \t]*```mermaid[^\n]*\n([\s\S]*?)^[ \t]*```/gm

function markdown(dir) {
  return readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const path = join(dir, entry.name)
    if (entry.isDirectory()) return markdown(path)
    return entry.name.endsWith('.md') ? [path] : []
  })
}

const hashOf = (source) => createHash('sha256').update(source.trim()).digest('hex').slice(0, 16)
const target = (hash) => join(outDir, `mermaid-${hash}.svg`)

const wanted = new Map()
for (const path of markdown(join(root, 'content'))) {
  const text = readFileSync(path, 'utf8')
  for (const [, body] of text.matchAll(FENCE)) {
    wanted.set(hashOf(body), { body, path })
  }
}

mkdirSync(outDir, { recursive: true })

const stale = [...wanted].filter(([hash]) => force || !statSync(target(hash), { throwIfNoEntry: false }))
if (stale.length) {
  const work = mkdtempSync(join(tmpdir(), 'mermaid-'))
  try {
    for (const [hash, { body }] of stale) {
      const source = join(work, `${hash}.mmd`)
      writeFileSync(source, body)
      execFileSync(
        mmdc,
        ['-i', source, '-o', target(hash), '-e', 'svg', '-c', theme, '-b', '#0A0A0A', '-p', puppeteer],
        { stdio: 'inherit' },
      )
    }
  } finally {
    rmSync(work, { recursive: true, force: true })
  }
}

// Drop SVGs whose fence is gone, so the directory stays in sync with content/.
const keep = new Set([...wanted.keys()].map((hash) => `mermaid-${hash}.svg`))
const removed = readdirSync(outDir)
  .filter((name) => name.startsWith('mermaid-') && name.endsWith('.svg') && !keep.has(name))
  .map((name) => (rmSync(join(outDir, name)), name))

console.log(`mermaid: ${wanted.size} diagrams, ${stale.length} rendered, ${removed.length} pruned`)
if (removed.length) console.log(`pruned: ${removed.join(', ')}`)
