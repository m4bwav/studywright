# Tests

Manual: build both decks, play through in browser answering every 5th wrong; the miss must return and appear on the end review list with its answer. Passed 2026-11-10.

Script: `python scripts/test_verify_xp.py` and `python scripts/verify_xp.py` (XP never drops, never spent, separate from gold). Passed 2026-11-13.

Script: `python scripts/test_sw_objectives.py` (objective coverage in `sw.py check`). Passed 2026-11-14.

Script: `python scripts/test_sw_hooks.py` (hook key and bare-fact warning in `sw.py check`). Passed 2026-11-19.

Script: `python scripts/test_sw_names.py` (reward-name lint in `sw.py check` and `sw.py names`) and the new rate tests in `test_verify_xp.py` (easy picks must not pay more XP per minute). Passed 2026-11-20.

Script: `python scripts/test_sw_glossary.py` (glossary match logic, its JS twin under node, glossary check rules). Headless Chrome probe of the built states-of-matter sample (cards, viewport clamp, register switch). Passed 2026-11-21.
