---
date: '2026-09-20T00:00:00+08:00'
title: 'My Bank Locked Me Out for Typing Like a Human'
description: 'Three typos and a branch visit later: why Malaysian banking apps treat you like a hacker and what I would do if Bank Negara let me near the rules.'
tags: ['rant', 'malaysia', 'banking', 'security']
---

Let me say this first so nobody gets confused. Malaysia is great. Food is elite, Grab shows up in four minutes, my MyKad renews faster than most countries ship a parcel. Then there is online banking, which feels designed by someone who has never forgotten a password in their life.

I use a password manager. I am the good user, the exact person every security blog begs you to become. Last Tuesday I tried to pay a bill at 11 PM. The manager filled in a 20 character monster, I reached for Enter, and my finger landed on the backslash key sitting right next to it. Tried again. Backslash. Third time, same key, because at 11 PM my hand runs on autopilot. Three wrong tries. Account blocked. Not slowed down. Blocked. My reward for doing security correctly was getting locked out over a key that lives one centimeter from Enter.

<figure>
<img src="/images/memes/meme-bank-pikachu.jpg" alt="Surprised Pikachu meme about backslash typo locking the account">
<figcaption>Shocked that backslash is not part of my password.</figcaption>
</figure>

## Three strikes and you take a number

Somewhere a committee decided three wrong passwords means you are a criminal. Not a tired human paying a bill in bed. A criminal.

Real attackers do not sit there typing your password by hand three times. They steal sessions, phish logins, buy leaked databases. The three strike lockout stops none of that. It only stops me, the guy who actually owns the money, from reaching my own money.

<figure>
<img src="/images/memes/meme-bank-skeleton.jpg" alt="Waiting skeleton meme about bank hotline hold music">
<figcaption>Me on hold with the bank, aging gracefully.</figcaption>
</figure>

The reset ritual is the best part. Call in, listen to six menu options, press 3 for internet banking, wait twenty minutes, answer your mother's maiden name like it is a spell, then get told to visit a branch anyway. At the branch you take a number, sit under fluorescent lights next to a poster that says "Banking Made Easy," and wait while three counters sit empty. The bill went out a day late because my own bank detained my account like a suspicious suitcase.

Now imagine it is Saturday and you actually need the money right now. Flight tickets about to sell out. A clinic deposit. Your car died in a mall parking lot and the tow guy takes transfer only. You open the app, typo the password, locked. The app helpfully offers two options: call the hotline or visit a branch. The branch opens Monday. The hotline puts you on hold until your phone battery gives up first. So you just sit there, a grown adult with money, unable to spend your own money, because a computer somewhere decided three typos equals fraud. Weekend does not exist in the rulebook. Urgency does not exist either.

Oh, and the hotline only works on weekdays. Locked out on a Saturday night? Your money is on leave until Monday morning. And when you finally reach a human, every call opens with a seven minute recording about beware of scammers. Seven minutes. I timed it once out of spite. Think about that. The scammers run a 24/7 operation with instant response times, and my bank needs office hours plus a podcast episode before I may touch my own salary. The criminals have better customer service than the bank. Let that sink in.

<figure>
<img src="/images/memes/meme-bank-bernie.jpg" alt="Bernie meme about the seven minute scammer warning">
<figcaption>Bernie has been on hold since Friday.</figcaption>
</figure>

If I ran Bank Negara for one week, this rule would be gone. Keep the account open and slow the attacker down instead. Wrong password? Wait five seconds. Wrong again? Wait thirty. Add a proper second factor and let the human keep trying. Every big tech login on earth does this. Only banks treat a typo like a confession.

## Binding device, or how to punish people for owning two phones

Then there is device binding. For the uninitiated: your banking app marries one phone. Get a new phone, reset your old one, or log in from your tablet, and congratulations, you are single again and the app wants a full re-verification ceremony.

<figure>
<img src="/images/memes/meme-bank-drake.jpg" alt="Drake meme rejecting device binding and approving passkeys">
<figcaption>Drake said what every banking user thinks.</figcaption>
</figure>

Who asked for this? My email does not do this. My money in an e-wallet does not do this. Only the bank app, holding the most important account I own, decided the fix for account takeovers is chaining my account to one slab of glass that I will drop in a toilet within two years.

And the ceremony to bind the new device is always the same adventure. SMS code that arrives ten minutes late. ATM card PIN. A cooling period of twelve hours where transfers are limited "for your safety." My safety would be fine with a passkey. My face plus my fingerprint plus a hardware key, synced across my devices, phishing resistant, no SMS to intercept. The technology exists. It ships on the same phone the bank just unbound me from.

The bank built its own worse version of MFA and named it binding. That is like inventing a square wheel and banning round ones.

The dumbest version of this happened when my old phone died for real. Black screen, no boot, a proper brick. I got a new phone, opened the bank app, and it asked me to approve the new device from the old device. The old device is dead. That is the whole problem. The money I needed for the phone was sitting inside the dead phone, guarded by an app that needed the dead phone to let it out. So I walked to an ATM, and the machine informed me I could only take out a small daily amount, like my own salary is a controlled substance. My money was right there behind the glass and the bank handed me pocket money.

<figure>
<img src="/images/memes/meme-bank-panik.jpg" alt="Panik Kalm Panik meme about approving a new phone from a dead phone">
<figcaption>The three stages of a dead phone.</figcaption>
</figure>

And after surviving all of that, the cooling period. You rebound the device, spelled your mother's maiden name to a robot, proved you are you six different ways, and the bank says: great, now wait twelve hours before moving your own money. What exactly is cooling down? The money was never hot. I was verified, rebound, quizzed, and documented. The cooling period is a waiting room after the waiting room. Fraudsters do not sit politely through cooling periods. They recruit mules and wait it out. The only person being cooled is me, staring at an urgent transfer and a countdown timer.

<figure>
<img src="/images/memes/meme-bank-cooling.jpg" alt="Always has been meme about the twelve hour cooling period">
<figcaption>Twelve hours. For safety.</figcaption>
</figure>

<figure>
<img src="/images/memes/meme-bank-buttons.jpg" alt="Two buttons meme about calling the bank or visiting a branch">
<figcaption>Every banking problem ends at this exact screen.</figcaption>
</figure>

## The OTP fossil record

SMS codes are the bank's favorite time machine. The code expires in five minutes and arrives in ten. By the time my phone buzzes, the code is a historical document. I type it in anyway, hoping the server shares my optimism. It does not.

The replacement is Secure Verification, where the app asks you to approve a transaction on the same phone within seconds. Miss the window because you were holding groceries, driving, or blinking, and you start over. Security that fails when your hands are full is not security. It is a reflex test with money on the line.

<figure>
<img src="/images/memes/meme-bank-otp.jpg" alt="Sad Pablo Escobar meme about waiting for an expired OTP">
<figcaption>Still waiting. The code gave up before I did.</figcaption>
</figure>

## My phone is a tool, not a crime scene

Some banking apps refuse to open if developer options or USB debugging are on. I am a developer. Half my friends are developers. Our phones have dev settings on the way chefs own knives. The bank sees the knife and calls the police.

The logic seems to be that debugging tools help malware, so nobody may have them. By that reasoning browsers should be banned because phishing exists. Block the actual malware behavior instead of frisking my settings menu. Until then, every bank update day means toggling my own phone off and on like I am smuggling something, which is exactly how a legitimate customer should feel.

<figure>
<img src="/images/memes/meme-bank-rollsafe.jpg" alt="Roll Safe meme about blocking developer phones">
<figcaption>Can't get hacked if the app never opens. Problem solved.</figcaption>
</figure>

## Small limits and nightly naps

The default transfer limit is sized for buying lunch, not running a life. Need to pay an invoice bigger than lunch? That is three days of transfers, or a trip to an ATM to raise the limit. My money has a bedtime and I need permission to change it.

And every night the banks go down for maintenance, always announced, always at the exact hour you finally remember the bill. The scammers from the seven minute warning never do maintenance. Their uptime shames actual infrastructure companies. Maybe play the warning recording on the maintenance page. At least someone would read it.

## New number, new identity crisis

Change your phone number and every bank treats you like a stranger wearing your face. Re-verify at an ATM or a branch, in person, carrying cards and documents, because apparently phone numbers are souls and yours just transmigrated. The irony is that recycled numbers are a real attack path: your old number goes to a stranger who now receives your OTPs. The bank knows this. Its solution is a queue ticket. The vulnerability is digital, the fix is furniture.

## The roach motel and the fee zoo

You can open an account online in minutes, smiling into your camera for liveness detection. Try closing one. That requires a branch visit, forms, and a chat with someone whose job is to ask why. Accounts check in online and check out in person. Roach motel banking.

<figure>
<img src="/images/memes/meme-bank-changemind.jpg" alt="Change My Mind meme about closing accounts online">
<figcaption>Closing an account takes one click. Change my mind.</figcaption>
</figure>

While you are trapped inside, the fees graze. Fall below some minimum and pay up. Leave the account alone and pay dormancy for the crime of not visiting. Once a year the credit card charges an annual fee and you call to beg a waiver like a peasant asking the king for bread. The call takes twenty minutes. The waiver is always granted, which raises the question of why the fee exists at all. It exists because some people forget to call. That is the entire business model, and it works.

<figure>
<img src="/images/memes/meme-bank-harold.jpg" alt="Harold meme about the annual fee waiver call">
<figcaption>Smiling through the annual fee waiver call.</figcaption>
</figure>

## The lifeboat is inside the locked cabin

Credit where it is due: BNM forced every bank to add a kill switch that freezes your account when things look wrong. Genuinely good idea. Now find it. It lives three menus deep inside the app, behind the same login that just locked you out over a backslash. The emergency brake only works if you can already drive the car. Put the kill switch on the login screen, no login needed, big red button. Emergencies do not carry passwords.

## If Bank Negara handed me the stamp for a week

One, kill the three strike lockout. Replace it with progressive delays plus real MFA. Attackers use bots, and bots hate waiting. Humans typo, and humans can wait five seconds.

Two, kill SMS codes as the only second factor and ship passkeys. Let me approve a new phone with biometrics from the old phone, or at a branch kiosk once, instead of this SMS plus card plus prayer combo. SMS interception is the oldest trick in the book and banks still treat it like a vault.

Three, stop punishing new devices and start scoring risk properly. New phone plus same face plus same SIM plus small transfer to a saved payee is me. New phone plus new SIM plus 2 AM plus max limit to a fresh account is not me. Block the second one. Wave the first one through. This is basic stuff and every fraud team knows it.

Four, publish the rules. Tell me exactly what locks an account, how long it lasts, and how to unlock it without a branch visit. Right now every bank has secret tripwires. You find them by stepping on them.

Five, run the hotline every day and kill the seven minute warning for callers who already verified themselves. Play it once, or stick it on the website. A lecture nobody can skip is not security. It is a podcast with one listener, and he hates it.

Six, stop cooling down verified users. A twelve hour freeze makes sense for a brand new payee receiving your life savings. It makes no sense after I rebound a device, passed every check, and send money to the same saved payee I have used for three years. Cool the risky transfers, not the routine ones.

Seven, put the kill switch where locked-out people can reach it: on the login screen, no password needed. An emergency tool behind a login is decoration.

Eight, let me close accounts online and kill fees that are always waived anyway. If every waiver call ends with yes, the fee is a memory test, not a price.

> "You shall not pass!", Gandalf (2001). Me, to my own login screen, holding the correct password on the fourth try.

## Credit where it is due, Malaysia is genuinely good

None of this changes the fact that I love living here. The sharia compliant accounts just work, and for Muslims who care about riba that clarity matters. You pick the Islamic window, the rules are stated upfront, no fine print games. Halal food everywhere with real certification you can trust, not vibes. The coffee shop owner remembers your order by day three. Strangers help you jump start your car in a mall parking lot and refuse money after.

Life admin here is easy in a way visitors always underestimate. Renew road tax on your phone, order nasi lemak at midnight, top up Touch n Go without thinking. The engineers building all of that are good. So why does the banking app feel like it was specified in 2009 and nobody is allowed to change the spec?

Nobody at the bank is evil. Someone is just scared, and scared people write strict rules instead of smart ones. Three tries and you are locked out feels safe in a meeting. Passkeys and risk scoring sound like work. So users pay the difference in queue numbers and hold music.

Fix the lockout, kill device binding, ship passkeys, and half the country stops dreading payday admin. Until then I will keep my branch queue ticket as a souvenir. Number 1047. They were serving 1003.
