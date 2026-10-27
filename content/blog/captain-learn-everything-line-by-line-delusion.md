---
date: '2026-10-25T21:00:00+08:00'
title: 'Captain Learn Everything and the Line-by-Line Delusion'
description: "A calm, measured response to 'learn everything,' 'you have no experience,' and 'IT is just reading code.'"
tags: ['opinion', 'career', 'engineering', 'rant']
author: nuh
---

Someone told me, with the confidence of a person who has never been on call, that you need to learn everything. Not everything in your lane. Everything. Every language, every framework, every branch of engineering, every obscure protocol, presumably including the bit of JavaScript that makes the printer work and the ritual that keeps the build server alive.

I said no. You need the fundamentals, a map, and the willingness to go deep where it matters. They said no. Not "no, here is why." Just no. The conversation equivalent of a popup with one button.

So I said okay. This is that conversation, reconstructed from memory, spite, and the part of my brain that keeps receipts.

If this were a movie, this is where the record scratch happens. Unfortunately, it is a blog, so you get a heading instead.

For the record: I have six years in IT and one year in electronics. That does not make me automatically right. It does make me automatically tired. I am legally required to say I am not a doctor, lawyer, or emotional support cactus. I am a guy with a blog and a grudge.

<figure>
<img src="/images/memes/meme-learn-everything.jpg" alt="One Does Not Simply meme: one does not simply learn everything without learning anything deeply">
<figcaption>Four years of tutorials, zero shipped projects, one very confident opinion.</figcaption>
</figure>

## The four claims

Let's call them Captain Learn Everything. Not because they said it once. Because they said it with the confidence of someone who thinks a Wikipedia tab is a personality.

Their argument had four moving parts:

1. You need to learn everything.
2. You can't have an opinion because you don't have experience.
3. Only electronics are complex. Cars are simple except F1.
4. IT is easy because you can read the code line by line.

Four claims. Four chances to be wrong. A hat trick plus one.

## Claim one: learn everything

Learning everything is not a strategy. It is a threat you make to yourself at 2 AM.

Knowledge is not a finite checklist. It is an ocean with a search bar. The moment you say "I will learn everything," you have signed up for a race with no finish line, no medal, and a LinkedIn post at the end.

Fundamentals are different. Fundamentals are compression. Ohm's law, Kirchhoff's laws, Boolean logic, data structures, protocols, feedback loops, incentives, failure modes. They are the load-bearing walls. Learn those and you can add rooms. Learn everything and you have a pile of bricks and no house.

This is the part where someone says "but a generalist knows a little about everything." No. A generalist knows enough about adjacent fields to ask better questions and learn the next thing faster. That is not the same as collecting tutorial badges like a raccoon collecting shiny objects. One is a skill. The other is a hoarding problem with a certificate.

The useful shape is not "knows everything." It is broad enough to talk to other people, deep enough to be useful, and honest enough to say "I don't know, give me twenty minutes and a search engine." That last part is doing more work than most résumés.

<figure>
<img src="/images/memes/meme-complexity-brain.jpg" alt="Expanding Brain meme: learn everything, learn the fundamentals, learn fundamentals and specialize, argue with someone who calls reading code a strategy">
<figcaption>The final panel is not enlightenment. It is just a meeting that should have been an email.</figcaption>
</figure>

## Claim two: you have no experience

Then they said I don't have experience, so I don't have the right to talk.

I have six years in IT and one year in electronics. But here is the thing: experience is not a magic wand. It is a collection of scars and shortcuts. It helps you recognize patterns. It does not make you correct. A senior engineer can be wrong. A junior can be right. The code does not check your résumé before it segfaults.

Experience is useful. It tells you which error message is a lie, which vendor is a lawsuit with a logo, and which "small change" will page you at 3 AM. It does not let you skip the argument. If your position is "I am older, therefore I win," you are not debating. You are doing a status check.

And the move itself is weird. "You don't have experience" is not a counterargument. It is a bouncer. It is a way to avoid the actual claim. If I say the sky is blue and you say I don't have a meteorology degree, the sky is still blue.

Also, six years is not a lifetime. It is enough to have seen a few disasters and learned their names. I have seen a production database held together by a cron job and a prayer. I have seen a printer achieve sentience and demand a sacrifice. I have experience. It is not the kind you put on a certificate. It is the kind you put on a t-shirt that says "I survived the migration."

## Claim three: only electronics are complex

Then came the car thing. They said only electronics are complex. Cars are simple, except F1. And when cars are complex, it is because of electronics.

This is the kind of statement that sounds smart until you open the hood and a spring hits you in the face.

Cars are complex in ways that have nothing to do with electronics: thermodynamics, materials, fluid dynamics, structural safety, manufacturing tolerances, emissions, supply chain, human factors, regulation, cost, and the fact that a family car has to start in a Malaysian afternoon and a Finnish winter and keep working for fifteen years while being maintained by someone who thinks "torque" is a type of cheese.

F1 is not "the complex car." F1 is a different complexity. It is performance under extreme constraints. A road car is complexity under mass production, safety, cost, and reliability. A truck is complexity under load and duty cycle. An EV is complexity in battery chemistry, thermal management, and charging. A car factory is complexity in logistics at a scale that makes your microservices diagram look like a grocery list.

And yes, modern cars have plenty of electronics. Dozens of ECUs, networks, sensors, software. But the electronics are not floating in the void. They talk to mechanical systems. They fail in mechanical ways. They are part of a system. That is the point.

Complexity is not a ladder with electronics at the top. It is a graph with axes: scale, coupling, uncertainty, safety, cost, latency, legacy, human factors. A family car and an F1 car are both complex. They are just complex in different directions. So is a hospital, a tax code, a power grid, and your family group chat.

<figure>
<img src="/images/memes/meme-car-complexity.jpg" alt="This Is Fine dog meme: cars are simple, only electronics are complex, while a modern car has dozens of ECUs and a software team">
<figcaption>The check engine light is not a decoration. It is a cry for help with a CAN bus.</figcaption>
</figure>

Here is a tiny slice of the graph:

| System | Main complexity |
|---|---|
| F1 car | performance under extreme constraints, aerodynamics, hybrid power, tires, regulations |
| Family car | safety, reliability, cost, mass production, supply chain, emissions, service life |
| IT platform | concurrency, state, dependencies, legacy code, security, humans |
| Power grid | real-time balance, safety, regulation, aging infrastructure |
| Tax code | everything, including the parts written by people who hate you |

Notice that none of these are "electronics versus everything else." They are different shapes of hard.

## Claim four: IT is just reading code line by line

This one is my favorite. They said when you have a problem in IT, you can just read the code line by line. As if the code is a novel with a beginning, middle, and end, and the bug is a typo on page 47.

Reading code line by line is necessary. It is also the bare minimum. It is like saying the way to fix a car is to look at the engine. Yes. And then what? Which part? Why is it making that noise? Why only on Tuesdays? Why does it stop when the customer walks in? Why does the error disappear when you add a print statement, like a quantum particle being observed?

Production systems are not a single file. They are distributed systems with concurrency, retries, timeouts, caches, queues, databases, third-party APIs, DNS, TLS, permissions, data migrations, legacy code, and a load balancer that is having a bad day. The bug is not always in the line. It is in the interaction between lines, services, machines, and humans.

Read the code line by line. Sure. Which code? The application? The framework? The library? The kernel? The network stack? The database driver? The code that was deleted three years ago but still runs because nobody turned off the cron job? The code in the configuration file that is technically not code but can still ruin your week? The code in the vendor's black box that you cannot read because it is a black box? That code?

Also, reading code tells you what the code does. It does not tell you what the system is supposed to do. Requirements are often wrong. The spec is a rumor. The ticket says "small fix." The user says "it just stopped working." The logs say nothing. The metrics say everything is fine. The dashboard is green. The users are not. This is the gap where senior engineers live.

If reading code line by line solved everything, debugging would be a book club. It is not. It is a hostage negotiation with a stack trace.

<figure>
<img src="/images/memes/meme-read-code-buttons.jpg" alt="Two Buttons meme: read the code line by line or accept that production is a haunted house, with a sweating person labeled me on call at 3 AM">
<figcaption>One button is a coping mechanism. The other is a lifestyle.</figcaption>
</figure>

## What I actually mean by fundamentals

Here is the boring part, which is also the point. I am not against learning. I am against the word "everything" doing the work of a plan.

Fundamentals are the things that transfer. In IT: data structures, algorithms, networking, operating systems, databases, security, distributed systems, debugging, testing, version control, and communication. In electronics: Ohm's law, Kirchhoff, AC and DC, components, datasheets, signal integrity, power, grounding, and how to use a meter without becoming part of the circuit. In cars: thermodynamics, mechanics, materials, control systems, safety, manufacturing. In any field: how to ask a good question, how to read a spec, how to test a claim, and how to admit you don't know.

Then you go deep in one or two areas. The rest you learn on demand. That is not laziness. That is prioritization. You have a finite brain and a finite weekend. The universe has infinite documentation. You need a strategy, not a guilt trip.

Generalists are not people who know nothing. They are people who know enough about adjacent fields to ask better questions. Specialists are not people who know everything about one thing. They are people who know where the bodies are buried in one thing. Both are useful. The worst is the person who knows just enough to be loud.

## The real argument

The truth is, this was never about learning. It was about status.

"Learn everything" is a flex. "You have no experience" is a gate. "Only electronics are complex" is a hierarchy. "IT is easy" is a dismissal. The whole conversation was a ladder, and they wanted to be on top.

I don't need to be on top. I need to be correct. And when I'm wrong, I need to find out before the outage does. That is the job. The job is not to win the conversation. The job is to build something that works, or to fix something that doesn't, or to explain why it can't be fixed without a budget and a small miracle.

Also, "you don't have experience" is a weird flex from someone who thinks reading code line by line is a debugging strategy. I have six years of IT experience. I have one year of electronics. I have enough experience to know that both fields are hard, and that anyone who says "just read the code" has never been on call for a system that reads back.

## The part where I stop being polite

So no, I don't need to learn everything. I need to learn the fundamentals, go deep where it counts, and know when to ask for help. I need to respect complexity without worshipping it. I need to treat experience as a tool, not a crown. And I need to stop arguing with people who treat confidence as a substitute for evidence.

If you are the person who said this to me, and you are reading this: hi. I hope your code compiles on the first try. It won't. And if you think it will, you have not learned enough yet. That is not an insult. That is the job.

Anyway. I have six years in IT and one year in electronics. That is not a flex. That is a warning label. Please do not hand me a soldering iron and a deadline in the same week.

Post-credits scene: they reply in the comments. I read it line by line. I find no evidence. I close the tab. The end.
