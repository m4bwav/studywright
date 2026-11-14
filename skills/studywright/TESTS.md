# Tests

Manual: build both decks, play through in browser answering every 5th wrong; the miss must return and appear on the end review list with its answer. Passed 2026-11-10.

Script: `python scripts/test_verify_xp.py` and `python scripts/verify_xp.py` (XP never drops, never spent, separate from gold). Passed 2026-11-13.

Script: `python scripts/test_sw_objectives.py` (objective coverage in `sw.py check`). Passed 2026-11-14.
