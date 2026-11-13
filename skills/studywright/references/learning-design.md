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

## Match the question to the kind of content

| Content | What the student must do | Question or game form |
|---|---|---|
| Facts (names, dates, terms) | recall it on cue | typed recall, then mc with near-miss lures; speed rounds and the boss timer fit here |
| Concepts (a category: "mammal", "solid") | sort new cases in or out | mc of fresh examples and non-examples; "which one is NOT a..."; sorting by tapping |
| Rules and principles (cause and effect) | predict what happens | "what happens if..." scenarios, why-questions, steps after a miss |
| Procedures (a method with steps) | carry it out | lesson mode: worked example, faded steps, solo with generated numbers |

A deck usually mixes all four; pick the form per item, not per deck.

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

## Ideas not built yet

- World mode: `steps` (smaller sub-questions after a miss), more for merchants to sell (built in 0.10.0: potion, trail map, compass, fact keepsakes; not built: hero cosmetics, selling back), level-up feat picks inside the world, region labels for other decks on the map.

- Gear or titles for mastering a whole deck (e.g. "Naturalist" title after a 90%+ follow-up).

- Co-play: a parent or sibling plays alongside (takes turns, or answers a different deck on the same screen); talk about the answers is where much of the learning happens.

- Around-the-game lesson note: a short printed or on-screen note for the parent with what the game covers and two questions to ask at dinner, so the game sits inside a lesson rather than replacing it.
