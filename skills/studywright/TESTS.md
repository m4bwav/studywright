# Tests

World deck check (run in the page console on 127.0.0.1 after a build; passed 2026-11-12 for texas-independence and selective-breeding): flood-fill from the start over walkable tiles (g f s G r D c) and count the deck's `Q` tiles touched; it must equal the number of questions. This caught a creature walled in by three others. With merchants (0.10.0) the same flood-fill must also touch one `M` tile per region that has `merchant` (8 of 8 and 90 of 90 for texas-independence, 2026-11-12); in the page also buy each kind of good and check gold, `hero.inv.items`, `S.bought`, the compass text in `#cp`, and a miss at 1 heart with and without a potion.

Manual: build both decks, play through in browser answering every 5th wrong; the miss must return and appear on the end review list with its answer. Passed 2026-11-10.
