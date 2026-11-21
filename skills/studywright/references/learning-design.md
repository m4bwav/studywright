# Learning design for study games

Rules the engine and decks follow, with the evidence base they come from. Check and extend in each refresh (RESEARCH.md).

| Rule | Where it shows | Basis |
|---|---|---|
| Ask, do not show: every item is a retrieval attempt | whole game | Testing effect / retrieval practice (Roediger & Karpicke 2006; Dunlosky et al. 2013 rate practice testing "high utility") |
| Feedback right after each answer, with the reason | `explain` panel | Feedback with explanation beats right/wrong only (Butler, Godbole & Marsh 2013) |
| A miss comes back 3 items later, until right | requeue in `answer()` | Spacing and successive relearning (Rawson & Dunlosky) |
| Typed recall as well as multiple choice | `type` questions | Generation effect; recall is harder and more durable than recognition |
| Distractors are real misconceptions | deck writing | MC with competitive lures can still drive retrieval (Little & Bjork) |
| Mix topics (shuffled order) | `shuffle` of the queue | Interleaving |
| No lives, no game over; streak is the only thing lost | HUD | Low-stakes testing keeps anxiety down; failure must stay cheap |
| Rewards attach to correct answers and progress, are visible and immediate | XP, levels, gold streak blocks, tower, sounds | Game feedback loops (juice) for motivation; keep extrinsic rewards light so they do not crowd out the learning |
| End with a review list of first-try misses, with answers | finish screen | Points study time at what is not known yet |

## Hero and RPG layer (0.3.0)

- One persistent character across games gives a sense of long-term progress (competence) and lets the student choose (autonomy): class, name, which feat or stat at each level-up. Mark asked for D&D style feats and Kingdom Come Deliverance 2 style learn-by-doing skills.
- Study areas rise two ways: by use (every 15 right answers, like KCD2) and by training picks at level-up (like a D&D ability bump).
- Guard rails: feats change XP or give one strike-out hint per quest; none skips a question or hides the explanation, so the learning loop (retrieve, feedback, spaced retry until mastered) stays intact. Grit rewards getting a missed question right later, which praises fixing mistakes.

## Built in 0.5.0

- Day-2 warm-up: each finish stores that run's first-try misses per deck; the next run serves them first and the title screen says so.
- Boss round: after the main run, first-try misses come back once more, each on a timer (20 s choice, 30 s typed). Retrieval under light pressure; +15 XP per hit, no requeue, score unchanged, result in the record as `boss`. Skippable.
- Read-aloud: a "Read it to me" button speaks the question and the choices in on-screen order (speechSynthesis).

## World mode (0.8.0; the game moved out to studyquest on 2026-11-12, the lessons stay here)

- Mark asked for an open world instead of a roguelike path: free movement, a land that is mapped and built up from game to game, the same hero everywhere. Autonomy (where to go next) and visible long-term progress (the map, buildings that grow on replays) are the motivation; the learning loop is unchanged.
- Teach before testing: each region's signpost holds the sheet's notes, and a question can open them without penalty. A miss shows the reason, then the creature refuses to be asked again until another question has been answered (spacing), and returns in a new wording (variants), so the retry is retrieval, not echo.
- Keys come only from mastering a whole region, and the hall holds mixed apply questions, so the ending is gated by learning, never by exploring.
- No game over: zero hearts sends the hero back to camp with full hearts and nothing lost.
- Every play ends with a log and a notes prompt (see SKILL.md, Paper trail), so results reach the notes without the parent retyping them.
- Built in studyquest (2026-11-12/13): `steps`, smaller sub-questions after a first miss. Practice only (no heart lost, no score), shown once per question, and the reworded retry still comes later, so the steps scaffold without replacing retrieval.
- Level-up picks in the world (training or a feat). The pick card waits until no other card is open and takes clicks only, because a held movement key (WASD) would otherwise choose for the player.
- Cosmetics for gold: hats, capes and companions, seeded per merchant so shops differ. Nothing sold touches a question, so gold can never buy an answer.

## Match the question to the kind of content

| Content | What the student must do | Question or game form |
|---|---|---|
| Facts (names, dates, terms) | recall it on cue | typed recall, then mc with near-miss lures; speed rounds and the boss timer fit here |
| Concepts (a category: "mammal", "solid") | sort new cases in or out | mc of fresh examples and non-examples; "which one is NOT a..."; sorting by tapping |
| Rules and principles (cause and effect) | predict what happens | "what happens if..." scenarios, why-questions, steps after a miss |
| Procedures (a method with steps) | carry it out | lesson mode: worked example, faded steps, solo with generated numbers |

A deck usually mixes all four; pick the form per item, not per deck.

## Encoding aids (mnemonics) for bare facts and lists

Retrieval practice tests what is stored; these help store a hard bare fact in the first place. Use them for facts and ordered lists only, not for concepts, rules or procedures, and not on every deck: each costs a few minutes of teaching.

- Hook: tie a bare name, date or word to something meaningful. "Baker" the name is forgotten where "a baker" the job is kept, because the job links to known ideas (ch. 2). Optional per-question key `hook` (one line: the image or the link). Show it after a first miss, never before the first try, so retrieval stays first. `sw.py check` warns when a deck has 5+ typed-recall items and no hook. Showing it in game.html is not built yet.
- Vivid, acting image: funny, gross-silly or exaggerated, the item doing something (ch. 5). Never adult or violent, whatever the classical advice says. A hook the child makes up or picks from two or three beats one handed over.
- Abstract words need a concrete stand-in first; nonsense or abstract items are the hardest to encode (ch. 6).
- Ordered lists (planets, steps, a sequence of rulers): a route lesson, one item per spot on a place the child knows well (their home, the game map), recalled by walking it in order. The place supplies the order the items lack (ch. 5). Not built.
- Gist before verbatim: test the meaning first; ask for exact wording only where the wording is the point (a definition, an assigned poem). For a poem or speech, one image per line or point, and lean on the rhyme and rhythm it already has (ch. 6).
- Chunking needs the pattern already known: teach the rule before a long sequence that uses it (ch. 3).
- Source: Joshua Foer, Moonwalking with Einstein (2011), ch. 2, 3, 5, 6. A journalist's account; the method is well supported for lists and ordered items, less for understanding. Book rules, unverified by a play test, except the hook warning.

## Illusions of knowing, try-first and cumulative review (Make It Stick)

- Sure or guessing: an optional toggle before feedback on key-idea items (not on every item: a click each tires a child). Records list sure-and-wrong items first; those are the illusions of knowing that rereading never reveals (ch. 1, 5). Not built.
- End-of-round re-ask: keep the instant reason, and at round end ask each missed item once more before showing its answer. Do not drop instant feedback; long delays let a wrong answer set in (ch. 2). Not built.
- Try first in lessons: one unscored attempt at a problem not yet taught, before the worked example; never score it (ch. 4). After the example, state the rule in one line and group the review's misses by rule (ch. 6). Not built.
- Two surface forms per key idea: `variants` must change numbers, setting or wording frame, not only reword the stem. Math and science decks also get "which method fits?" items, the skill a blocked set never asks for (ch. 1, 3).
- Cumulative follow-ups: a follow-up deck re-asks a sample from every earlier deck in the unit, not only the last one's misses; predictable, frequent, low-stakes quizzes (ch. 8, sec. 31).
- Leitner level per item: records keep a level per item across plays; a miss drops it to level 1 and it returns next session, mastered items rarely (ch. 3). Not built.
- Praise effort, strategy and recovery ("you fixed it on the second try"), never traits ("smart", "genius"). `sw.py check` warns on trait words in `win`, `explain`, `scene`, `intro` and `practice` (ch. 7). Growth-mindset effects replicate smaller than first claimed: keep the wording, build nothing more on it.
- Tell the child why it feels hard: one line on the intro or finish that mixed, spaced practice feels slower but sticks (ch. 3).
- No false premise: a question's wording, or a wrong choice's setup, must not assert something false or plant a vivid wrong detail; it can be recalled later as fact (ch. 5).
- Too easy teaches nothing: a lesson at 100% first-try accuracy over several plays is errorless pacing; make the steps bigger (ch. 4).
- Source: Brown, Roediger, McDaniel, Make It Stick (2014). Book rules, unverified by a play test, except the praise warning.

## Speed and plateaus

- A speed round's target is the child's own best time cut by 10 to 20 percent, not one fixed timer; the boss timer's fixed 20/30 s is a starting value. The figure is one coach's instruction, not a measured optimum: measure (Foer ch. 8).
- A mastered deck replayed at the same difficulty is a plateau. Offer a "hard ones" round built from recent misses instead of a replay of the whole deck.
- Source: Foer ch. 8 (the OK plateau, after Ericsson). Not built; unverified.

## Writing multiple-choice items

`sw.py check` warns (never fails) on the cheap ones: a choice much longer than the others, and "all/none of the above".

- [ ] Choices are about the same length and grammar; the right one is not the longest or the most careful.
- [ ] One answer is clearly best. A "good vs better" item is fine only when the prompt says so ("which is the BEST reason") and `explain` says why the others fall short.
- [ ] Every wrong choice is a mistake a student really makes (see Distractors above), not filler.
- [ ] A concept item includes non-examples that look like examples (a whale for "fish"), so it tests the idea and not surface features.
- [ ] No "all/none of the above", no double negatives, no clue words shared only by the prompt and the answer.

## Before and after a session

- Pre-brief: the title screen says in one line what this run practices ("telling melting from dissolving").
- Debrief: after the review list, ask one question back ("Which one will you look at again before the test?"). It goes into the notes prompt.
- Beside the score show a word for the skill level (Starting, Getting there, Solid, Mastered) so the number means something to a child.

## Measuring learning honestly

The in-game score rises with requeues and is not proof of learning. The honest signal is the delayed retest: the same item (or its variant) asked days later, first try only. The day-2 warm-up and follow-up decks give that; when reading records, compare first-try results for the same items across days, not scores across runs.

## Named failures to avoid

- Pointsification: points and badges bolted onto a dull quiz, with nothing interesting to do. Rewards must sit on top of real practice and a reason to care (the story, the hero).
- Badge inflation: a badge for everything means nothing; keep them few and tied to mastery.
- Rewards crowding out interest: for a topic the child already likes, heavy rewards can make it feel like work. Keep strong extrinsic rewards for dull drill (spelling, facts); let interesting material carry itself.
- For kids: no variable-ratio rewards (loot-box style random payouts), no scarcity timers or streaks that punish a missed day.
- Playtest: run one session with rewards turned off. If the child still plays and learns, the core is sound; if not, the rewards were carrying a weak game.

## XP, gold and progress bars

- XP only goes up and is never spent; gold is the currency you spend. Never pay gold from XP or buy XP with gold. `scripts/verify_xp.py` checks the templates (run it after touching an award).
- A progress bar never stops at a full 100%: when one fills, show the next tier (next level, next mastery tier, the follow-up deck) so there is always a next step.
- Idea not built: a "this week" XP count beside the lifetime total, so a slow week still shows effort without resetting anything.
- No public status or leaderboards: these are single-child offline games.
- Easy picks must not pay better: wherever the child chooses (which deck, mode, hint or no hint), XP per minute on the easier pick must not beat the harder one, because learners paid for right answers keep choosing easy problems after the pay stops (Kapp, ch. 4). `verify_xp.py` warns on it; with no arguments it checks game.html, where replaying a mastered deck pays about 150 XP/min against 47 for a new deck (time and accuracy guessed) until the taper below is built; `--rates TABLE.json` checks another engine's choices.
- Source: Zichermann and Cunningham, Gamification by Design (2011), ch. 3. Book rules, unverified by a play test; the XP rule has the script check behind it.

## Consent, endings and fair rewards (0.14.0)

- Play is offered, never assigned as a chore: the child can pause or skip a day with no penalty and no lost progress. Forced play tends to lower both mood and results.
- Campaign, not endless: each topic arc has a finish state the child can reach and leave (a delayed retest passed). After that, the deck is review on request, not a treadmill.
- Never devalue what was earned: do not raise level thresholds, reprice gear or hand out a badge to everyone after the fact. Change rules for new progress only.
- Every currency has somewhere to go: if gold piles up with nothing worth buying, add a sink or stop paying it.
- Same-task rule: rewards come only from doing the study itself (answering, retesting), never from a side chore added next to it.
- Competition check: if any versus or race feature is added (sibling co-play, a beat-your-time mode), ask what the weakest player gets from it; if the answer is nothing, make it cooperative or race against their own past score.
- Loophole pass before shipping a reward: write down the cheapest way to earn it without learning (guess-spamming, replaying an easy deck, quitting before a miss) and close it.
- Source: Brian Burke, Gamify (2014), ch. 7-8. Book rules, unverified by a play test or script check.

## Observe, assess, respond (0.15.0)

Any adaptive feature is written as three lines before it is built: what the game observes, what that is taken to mean, what changes. Each part can stay simple; rules are enough, no model needed.

| Observe | Assess | Respond |
|---|---|---|
| the choice picked, first try or not | the misconception tagged on that wrong choice (noted when the deck is written, below) | its explanation, then a retry or `steps` aimed at that mistake |
| a long pause before answering | low confidence, not a wrong idea | offer the notes or a hint, no penalty |
| first-try results for the same items across days | where the child sits against a target success band | change difficulty for the next session only |

- Tag each wrong choice with the misconception it catches. A deck can say it in the item's `explain`; when an item has several plausible lures, write one short line per lure so the explanation can name the mistake that was made.
- Difficulty moves between sessions, never mid-quiz. Live adaptation can raise stress for learners who cope poorly; a child should meet a stable run and a changed one tomorrow. Aim for a band where most first tries succeed but not all; the band numbers are ours to set by play test, the book gives none.
- Coverage: list the sheet's learning goals in the optional deck key `objectives` and tag questions with `objective`; `sw.py check` fails when a goal has no question or a question names an unknown goal.
- Questions an AI wrote get a check pass before the child plays: a second read (by the agent against the sheet, or by the parent) that each answer is right, each lure is wrong for a stated reason, and nothing contradicts the sheet. When a fact on the sheet changes, search the deck for every item that uses it.
- Source: Mangos and Ferraro (eds.), AI and Gamification Technologies for Complex Work Simulation and Training, ch. 3, 6, 7. The book is about adult, mostly military and workplace training; use with children is ours and unverified. Book rules, unverified, except the coverage rule, which `sw.py check` enforces.

## Ideas not built yet

- World mode (now in studyquest): selling back, region labels for other decks on the map.

- Gear or titles for mastering a whole deck (e.g. "Naturalist" title after a 90%+ follow-up).

- Co-play: a parent or sibling plays alongside (takes turns, or answers a different deck on the same screen); talk about the answers is where much of the learning happens.

- Around-the-game lesson note: a short printed or on-screen note for the parent with what the game covers and two questions to ask at dinner, so the game sits inside a lesson rather than replacing it.

## Retention, tapering rewards and child-written questions (0.16.0)

- Show mastery per topic as a retention bar, not a completion bar: it slowly drains while a topic goes unreviewed and refills on a correct first try, so the bar says what the child still knows today.
- Taper rewards as a topic is mastered: full reward the first time a concept is got right, smaller ones for repeats of items already mastered, so the rewards point at new learning. Rewards stay fixed and predictable; the variable-ratio ban above still holds.
- Optional: let the child write a question of their own for a topic. An adult checks it before it enters a deck; unchecked questions never reach play.
- Source: Ferro, Gamification with Unity 5.x (ch. 1, 10). Book rules, unverified by a play test; none is built yet.

## Sort into bins, a collection book and own-best times (studyquest, 2026-11-17)

- Classification ideas (tissue / organ / organ system; natural / artificial selection; myth / fact) test better as one sort question than as several two-choice items: every card must be placed, so guessing one answer does not pass, and partial credit (cards in the right bin) shows how close the student was. Built as `type: "sort"` in studyquest world mode.
- A collection book (one page per idea mastered, kept across replays) gives a visible, fixed-rule goal that also works as a review sheet: each page repeats the answer and the reason.
- Timing a region against the student's own best adds pace without comparison to others; keep it off scored questions and never punish a slower time.

## Homework finale and showing the working (studyquest, 2026-11-18)

- Homework finale: the real worksheet problems go in the deck marked `homework: true`. They stay off the map and are asked only by the final boss once every region is mastered, so the game teaches the method on its own practice items first (a teaching ladder built from the worksheet), then the homework is the climax. Answers are stored as a hash and graded by it; a miss reveals nothing and costs nothing, so the game never hands out the homework answers and the child still does the work. Typed numeric answers must match exactly (no fuzzy matching on numbers).
- Homework night, short form (2026-11-19): when the sheet is due tonight, about 10 warm-up items are enough: one for the rule in words, then one per step the sheet uses (find the angle, find the missing part, write the equation, x on both sides, plug x back in), each on new numbers that are not any of the sheet's answers. Then the sheet's own problems as the finale. Solve the whole sheet before writing the deck and check it against any built-in answer key (a riddle code, a matching table); a mismatch means a misread figure. Figures cannot go into finale items, so state each figure in words (which side is extended past which point, which angles are given) and say which sheet problem it is, so the child can look at the paper.
- Show how a number was reached: every number the game shows (damage, score, reward) appears as its sum of parts (move + gear, base + bonus). The child sees why the number is what it is, which is a small arithmetic lesson in itself and makes the rules learnable instead of magic.

## Reward names, two voices, feedback timing (Kapp, second pass, 2026-11-20)

- Feat, badge and title names are read like praise: no trait words, and never a mocking name for a miss; a near-miss award says "almost" kindly. `sw.py names` lints the engine files and `sw.py check` lints a deck's optional `feats`, `badges` and `titles`.
- Two voices: one character explains (the reason, the method) and a different one cheers (praise, streaks); do not fold both into one mentor line. Small studies, test with the child first.
- Fade feedback timing by mastery: first sight of an item always gets the instant reason; on review rounds of items already mastered the reason may wait until the round ends, so the child judges first. Small studies (adult lab), test with the child first.
- Source: Kapp, The Gamification of Learning and Instruction (2012), ch. 4 (rewards, avatars) and ch. 10 (notification, goal orientation). Book rules, unverified, except the name lint and the XP-per-minute warning.

## Help ladders, idle hints and input gates (measured on a live kids' game, 2026-11-20)

- Help ladder keyed to miss count for typed answers: each extra miss unlocks one more help (the sentence, then the spoken word, then the next letter), and the screen shows how many tries until the next help. Two presets: easier at 0/2/4 misses, harder at 3/5/7.
- Never ask a missed item again straight away. A game that drew the retry at random with 50% odds asked it immediately 47% of the time, so the child echoed an answer shown 2 s earlier. Keep the fixed "comes back 3 items later" spacing.
- Hold the miss feedback about 2.2 s with input locked, and after praise gate the advance for about 1.2 s, so a mashed key cannot skip either the reason or the praise.
- Co-play for mixed ages on one screen (adds to the co-play idea above): give the reader and the pre-reader different jobs, with idle hints after about 9-13 s for the pre-reader and about 30 s for the reader.
- Source: one open-source kids' word game played headless and timed (harvest notes, 2026-11-20). Numbers from that game, not yet play-tested here.
