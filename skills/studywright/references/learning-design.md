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

## Ideas not built yet

- Boss round: a timed final pass over first-try misses.
- Day-2 mode: reload remembers misses (localStorage) and starts with them (spaced across days).
- Read-aloud button (speechSynthesis) for younger readers.
- Two-player hot-seat for parent and child.
