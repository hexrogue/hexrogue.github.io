---
date: '2026-10-21T09:00:00+08:00'
title: 'Turnitin Flagged 19 Sentences. I Flagged Its Homework.'
description: 'A 26% AI score, 19 blue highlights, and a stack of research that Turnitin hopes you skip.'
tags: ['university', 'rant', 'ai', 'grading']
author: nuh
---

Twenty-two pages. Four thousand and forty-one words. A PDF opens and the introduction looks like someone lost a fight with a blue highlighter.

At the top, in the kind of font that expects to be taken seriously: 26% detected as AI. Nineteen blue chunks. That's it? That's the evidence? I have seen more rigorous accusations from a fortune cookie.

Turnitin: I also have a disclaimer.

Me: Of course you do.

The disclaimer says the assessment "may not always be accurate" and "should not be used as the sole basis for adverse actions against a student." Translation: the machine is allowed to be wrong, and the student is still allowed to be punished for it. That is a smoke alarm that admits it might not detect fire while your landlord bills you for the ashes.

<figure>
<img src="/images/memes/meme-turnitin-buttons.jpg" alt="Two Buttons meme: Trust the 26% versus reading the disclaimer, with a sweating person labeled me, with a bibliography">
<figcaption>The machine is allowed to be wrong. The student is still allowed to be punished for it.</figcaption>
</figure>

Maybe our report was 0% AI. Maybe it was 26%. The PDF doesn't prove either number. It proves a model produced a number with a font. Somewhere, a spreadsheet felt seen.

The highlights are visible. I'm not blind. The question is whether a blue sentence is evidence or a prediction wearing a highlighter. Turnitin's own paperwork says prediction. The grade says evidence, and the grade has a chair and a signature.

## The fine print is doing a lot of work

The report gives you a percentage, nineteen blue chunks, and a disclaimer. It does not give you the model version, the threshold, the per-sentence confidence, or the denominator. It is a horoscope with a logo, except a horoscope doesn't get to fail you. A 26% score is the chimichanga of evidence: deep-fried, structurally unsound, and somehow still on the menu.

Turnitin's FAQ says the percentage is not necessarily the percentage of the whole submission. The model only scores long-form prose. Bullet points, code, and short answers don't count. So 26% of 4,041 words is not 1,050 words. It's 26% of whatever the model decided was prose. The report doesn't show the denominator. That's like saying 26% of your car is broken and refusing to say which car. Or which 26%. Or whether the car exists. None of that is in the report.

<figure>
<img src="/images/diagrams/turnitin-26-percent.svg" alt="Diagram showing 4,041 words, the model selecting long-form prose, scoring overlapping chunks, and producing 26% of qualifying text, not 26% of the submission or a 26% chance of misconduct">
<figcaption>26% of what? The report would rather not say.</figcaption>
</figure>

A 26% AI score is also not a 26% chance you cheated. It's a prediction about a share of qualifying text. The PDF doesn't give you a probability of misconduct. Your grade does. Those are different things, and only one of them follows you to graduation.

The FAQ says individual predictions may not always be explainable in simple terms. So the student can't check the reasoning. The lecturer can't check the reasoning. The number is the argument, which is a system with less rigor than a fortune cookie.

The highlights look like sentences. The model scores overlapping chunks. A clean sentence in the report can be a chunk with a probability attached. The interface makes the output look more precise than it is. That is the job: persuasion. Somewhere, a dashboard is very proud of itself.

## The study Turnitin doesn't put on the box

Temple University tested 120 texts: 30 human-written, 30 AI-generated, 30 AI-generated and then run through paraphrasing tools, and 30 hybrid texts. They sent all of them through Turnitin and checked whether the blue highlights landed on the AI sentences.

They didn't, and the report says so plainly: "We saw no relationship between the sentences in the text that were flagged as AI generated and the sentences that actually were AI generated."

The highlight and the AI sentence are not on speaking terms, or even in the same group chat. This is the comic-book crossover where two heroes finally meet and discover they have nothing to say to each other.

On clean human texts, Turnitin got 28 out of 30 right. On clean AI texts, 23 out of 30. On disguised AI texts, 19 out of 30. On hybrid texts, the scores were a mess. The report says the tool is least effective on hybrid texts. Group reports are hybrid texts by default: five names, multiple drafts, citations, edits, maybe a grammar tool. The more complicated the text, the more decorative the highlight, like a spoiler on a rental car.

Product demos skip this bit because a clean 100% AI sample and a clean 100% human sample are easy mode. Students live in the messy middle, which is where the product falls apart.

## The detector has a type

Liang et al. ran 91 human-written TOEFL essays and 88 native English essays through seven detectors. The native essays were fine. The TOEFL essays were flagged at 61.3%. At least one detector flagged 97.8% of them. All seven agreed on 19.8%.

Then they asked ChatGPT to make the TOEFL essays sound more native. The false positive rate dropped to 11.6%. The essays and the humans stayed the same; only the vocabulary changed. The detector wasn't smelling AI; it was smelling an accent, and it was wearing a lab coat while it did it.

Academic writing is a register. I was taught to write it, and the detector flags it, while students who already sound like the model get a pass.

## Turnitin's report card

| Study | Score | Teacher's note |
|---|---|---|
| Temple: do the highlights match the AI sentences? | 0 relationship | The blue highlighter and the AI text are not on speaking terms. |
| Liang: human TOEFL essays | 61.3% flagged | Native essays: 5.1%. The detector has a type. |
| Weber-Wulff: 14 detectors, including Turnitin | Neither accurate nor reliable | The whole class failed. Turnitin included. |
| Perkins: 22 GPT-4 submissions | 91% flagged, 54.8% content identified | It knew something was wrong. It just didn't know what. |
| Hadra: 192 texts | 0.61 accuracy, 0.29 AI sensitivity | It missed 71% of the AI texts. Great at catching humans, though. |
| Turnitin's own sentence-level FPR | Around 4% | One in 25 highlights can be human. Sleep tight. |

Turnitin's overall accuracy in the Hadra study was 0.61. Its sensitivity for AI texts was 0.29. That's a D in any class that isn't graded on a curve by the vendor. Some studies find high accuracy on clean AI samples. Good for them. The hard part is the messy middle. Group work. Edits. Citations. Second-language writing. That's where the product falls apart. It is the 80s movie montage where the underdog wins by believing in himself, except the underdog is a spreadsheet and the trophy is your transcript.

<figure>
<img src="/images/memes/meme-turnitin-fine.jpg" alt="This Is Fine dog meme: Turnitin says it may be inaccurate while the grade is already attached">
<figcaption>The disclaimer says "may not always be accurate." The grade says "we'll take it from here."</figcaption>
</figure>

## The marketing department and the engineering department are in different group chats

Turnitin's 2023 press release says the tool "identifies 97 percent of ChatGPT and GPT3 authored writing, with a very low less than 1/100 false positive rate." That's a lab result on GPT-3 and GPT-3.5, the models Turnitin's first detector was trained on. It is not a classroom result from 2026. Classrooms are not the lab, and they have group chats.

The FAQ says the tool is "98% confident." Confidence is not accuracy. A model can be 98% confident and wrong. Turnitin's own 2023 blog says the sentence-level false positive rate is around 4%. The same company reports two numbers, and the better one is in the headline. This is the 80s action movie villain who says "trust me" right before the building explodes.

The product page says the tool has been enabled by 98% of its customers. That's adoption, not accuracy. It says "independent research shows very high accuracy." Some studies do. The independent study I found says 0.61 overall accuracy and 0.29 sensitivity for AI texts. The disagreement is about the messy cases. Marketing picks the sample; classrooms don't get that choice.

Turnitin is selling a probability to institutions that want a verdict. The product looks like the plagiarism checker: same interface, same highlight, same score. The plagiarism checker shows you the original source. The AI checker shows you a blue sentence and asks you to trust the model. It is a different evidentiary standard wearing the same uniform. In comic-book terms, it is a reboot with the same costume and a completely different origin story.

<figure>
<img src="/images/memes/meme-turnitin-brain.jpg" alt="Expanding Brain meme: plagiarism checker shows the source, AI checker shows a blue sentence, ask the student to prove a negative, attach a grade anyway">
<figcaption>Same interface, same highlight, same score. Different evidentiary standard.</figcaption>
</figure>

Turnitin's own FAQ says it does not make a determination of misconduct. It provides data for educators. The grade is the determination. That gap is where the damage happens, and it has a student in it.

## Five names, one score, zero attribution

There are five names on the cover of our report, one file, and one score.

The report cannot tell you who wrote the highlighted sentence. It cannot tell you whether the sentence came from a draft, a citation, a template, or the group member who writes like a textbook. It just knows someone in the group chat is in trouble. This is a comic-book crossover event: five heroes, one villain, and nobody can agree on canon.

If the lecturer wants to penalize an individual, the report can't support that. It can start a group conversation, but it can't assign blame. The workflow does that part for free.

Group work is normal. Shared documents are normal. Editing each other's sentences is normal. The tool was not built for that, and the report does not pretend to attribute authorship. The workflow does.

## Turnitin, buddy, read the room

A perfect detector is not on the table. I want one that can support the claim it is making.

1. Show the sentence, the model version, the threshold, and the per-sentence confidence. A blue highlight is not a receipt.
2. Show the denominator. 26% of what? Which words counted? Which words were skipped?
3. Group work: don't give one AI score to five people. The report can't tell you who wrote the sentence.
4. Use it to start a conversation, not to finish a grade. Your own cover page says so. The policy should match the cover page.
5. If you can't do that, don't attach a grade to it. A suspicion is not a rubric.

<figure>
<img src="/images/memes/meme-turnitin-simply.jpg" alt="One Does Not Simply meme: One does not simply treat a probability as evidence">
<figcaption>A blue highlight is not a receipt.</figcaption>
</figure>
The last point matters most: a grade needs a claim someone can check, and a highlight is a guess with a colour.

## The email is one line

Hi, lecturer. If you're reading this, I'm disappointed, and I have a bibliography.

The email is one line: "Which sentence, and what standard?"

If the answer is "the report says 26%," then the report is doing the grading. If the answer is "this sentence, and here's why," then we can talk. I can explain what I wrote, show my drafts, and answer the specific claim. I have notes. I have version history. I have time.

Turnitin says it may be wrong, so I'm asking the humans to read that part. It shouldn't be a difficult request. And if the humans still choose the number, at least we will all know what the number is worth. Probably less than the chimichanga.

## Sources

1. Salem, L., Fiore, S., Kelly, S., & Brock, B. "Evaluating the Effectiveness of Turnitin's AI Writing Indicator Model." Temple University. [PDF](https://teaching.temple.edu/sites/teaching/files/media/document/Evaluating%20the%20Effectiveness%20of%20Turnitin%E2%80%99s%20AI%20Writing%20Indicator%20Model.pdf)
2. Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). "GPT detectors are biased against non-native English writers." Patterns, 4(7), 100779. [DOI](https://doi.org/10.1016/j.patter.2023.100779)
3. Weber-Wulff, D., Anohina-Naumeca, A., Bjelobaba, S., Foltýnek, T., Guerrero-Dib, J., Popoola, O., Šigut, P., & Waddington, L. (2023). "Testing of detection tools for AI-generated text." International Journal for Educational Integrity, 19, 26. [DOI](https://doi.org/10.1007/s40979-023-00146-z)
4. Perkins, M., Roe, J., Postma, D., McGaughran, J., & Hickerson, D. (2024). "Detection of GPT-4 Generated Text in Higher Education." Journal of Academic Ethics, 22, 89-113. [DOI](https://doi.org/10.1007/s10805-023-09492-6)
5. Hadra, M., Cambridge, K., & Mesbah, M. (2026). "Evaluating the accuracy and reliability of AI content detectors in academic contexts." International Journal for Educational Integrity, 22, 4. [DOI](https://doi.org/10.1007/s40979-026-00213-1)
6. Chechitelli, A. (2023). "Understanding the false positive rate for sentences of our AI writing detection capability." Turnitin. [Link](https://www.turnitin.com/blog/understanding-the-false-positive-rate-for-sentences-of-our-ai-writing-detection-capability)
7. Turnitin. "Turnitin's AI writing detection capabilities FAQs." [Link](https://www.turnitin.com/products/features/ai-writing-detection/faq)
8. Turnitin. (2023). "Turnitin announces AI writing detector and AI writing resource center for educators." [Link](https://www.turnitin.com/press/turnitin-announces-ai-writing-detector-and-ai-writing-resource-center-for-educators)
