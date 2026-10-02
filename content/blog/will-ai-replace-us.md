---
date: '2026-10-02T00:00:00+08:00'
title: 'Will AI Replace Us? Nah, But It Will Expose Us'
description: 'Everyone panicking about AI taking jobs missed the point. AI wont replace you. Someone using AI will. My honest take as a dev.'
tags: ['ai', 'rant', 'career']
author: nuh
---

Ngl, I am tired of this question. Every family gathering now: "Nuh, AI can code already right? So programmers habis la?" Bro. Chill.

Yes, I use AI daily. Yes, it writes half my boilerplate. No, it has not replaced me. It just made the boring parts faster and the dumb parts more obvious.

## AI is a fast intern, not a senior

Give AI a clear task and it cooks. "Write me a CRUD API with auth, validation, tests." Done in 30 seconds. Crazy.

Give it a vague real-world problem and it folds. "Boss wants the report feature faster but customers complain the data is wrong and finance uses Excel from 2019." Good luck prompting that.

| Task | Speed | Quality |
|---|---|---|
| Boilerplate CRUD, regex, SQL joins | 30 sec | fine, read it first |
| Explain a stack trace | 10 sec | actually great |
| Vague ticket, three stakeholders | fast | confidently wrong |
| Prod incident, 3am | fast | do not touch it blind |

<figure>
<img src="/images/memes/meme-ai-intern.jpg" alt="Bad Luck Brian meme about reviewing AI code late at night">
<figcaption>Me at 2am. The import it invented does not exist.</figcaption>
</figure>

AI has no context. It does not know your client is lying, your database is cursed, your boss changed requirements in a WhatsApp voice note at 11pm. It predicts the next plausible token and says it with total confidence, which is the dangerous part. Sound right, be wrong.

I have caught it inventing libraries, hallucinating docs, confidently explaining code that does the opposite. Fast intern energy. Super helpful, needs supervision, cannot be left alone with production.

Real example from last week:

```text
BAD:  "write auth for my app"

GOOD: "Node 20 + Express 4. POST /login takes {email, password}.
       Check bcrypt hash in Postgres users table, return 401 on
       mismatch, sign JWT (1h expiry) on success. No extra deps."
```

The first one gives me a 200-line fantasy with `require("magic-auth")` that does not exist. The second one actually ships. Same model, different operator. Writing the spec well turned out to be the skill, not typing fast.

## The calculator did not kill mathematicians

We have been here before. Calculators did not kill math. Excel did not kill accountants. Stack Overflow did not kill programmers. Same panic every time, same outcome: the people who used the tool got better, the people who refused it got left behind.

AI is just the next one, louder. It ate the easy tickets. Boilerplate, the regex you were gonna Google anyway, that CSS centering demon, boring CRUD. Gone in seconds.

What is left is the actual job: figuring out what to build, what matters, what breaks at 2am, who to say no to.

<figure>
<img src="/images/memes/meme-ai-boilerplate.jpg" alt="Oprah you get a meme about boilerplate taking three hours versus AI taking thirty seconds">
<figcaption>Junior devs spending 3 hours on boilerplate. AI: 30 seconds.</figcaption>
</figure>

## Who actually gets replaced

Lowkey, harsh truth: AI will not replace devs. But devs using AI will replace devs who refuse to touch it.

Same for designers, writers, video editors, everyone. If your whole job is copy-paste, convert this to that, summarize this PDF, resize 100 images, yeah bro, you are cooked. Not because AI is smart, but because your job was already a script.

But if your job involves talking to messy humans, making judgment calls with incomplete info, taking blame when stuff explodes? You are safe for a while. AI cannot attend a 9am meeting and read the room. It cannot tell a client their idea is trash without getting fired. It cannot get paged at 3am and fix prod while half asleep.

The people panicking the loudest are usually managers who think coding is just typing. Nah. Typing was never the job. Thinking was.

## The Malaysian corner

Here? AI replacement is even funnier. Half our companies still run on paper forms, WhatsApp approvals, and one uncle who knows where the server password is. AI cannot replace you if the company has not gone digital yet.

What I actually see: bosses paying for ChatGPT Plus, then telling staff to "AI everything" with no training, no workflow, no clue. Then shocked when output is garbage. Bro, the tool is not the skill. Give a Ferrari to someone with no license, you still get a crash.

The ones winning are freelancers and small teams. One guy with AI now does the work of three. Quoting faster, shipping faster, undercutting agencies. That is the real disruption here, not robots stealing office chairs.

## What I do now (my survival guide)

Simple. I stopped memorizing syntax and started leveling up the stuff AI is bad at.

One, I prompt like a boss. Break big tasks into small ones. Give context, give constraints, tell it what NOT to do. Garbage in, garbage out still applies, just faster now.

Two, I review everything. AI code goes through me like junior PR. I run it, test edge cases, ask "why this?" If you blindly copy-paste AI output to prod, you are not a dev, you are a liability with WiFi.

Three, I learn fundamentals harder, not less. OS, networking, how HTTP actually works, how databases index stuff. Because when AI hands you broken code, fundamentals let you smell it in 10 seconds instead of debugging for 3 hours.

My loop for any AI-generated code, every time:

```bash
# does it run?
go vet ./... && go test ./...

# what did it actually change?
git diff --stat && git diff

# delete the clever parts I cannot explain in one sentence
```

<figure>
<img src="/images/memes/meme-ai-denier.jpg" alt="American Chopper argument meme about devs arguing over AI">
<figcaption>Still building it by hand. Also still copying from Stack Overflow.</figcaption>
</figure>

## The one sentence version

AI will not take your job, but it will delete the boring half of it and expose anyone who was only doing the boring half.

> "I am not a genius, I am just a smart man with a smart phone.", sort of what every AI power user is right now. Tools do not replace thinking. They amplify whoever is already thinking.