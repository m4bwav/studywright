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

## Ideas not built yet

- World mode: `steps` (smaller sub-questions after a miss), more for merchants to sell (built in 0.10.0: potion, trail map, compass, fact keepsakes; not built: hero cosmetics, selling back), level-up feat picks inside the world, region labels for other decks on the map.

- Gear or titles for mastering a whole deck (e.g. "Naturalist" title after a 90%+ follow-up).

