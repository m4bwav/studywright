# Handoff: studywright

State 2026-11-10: v0.2.0 public at https://github.com/m4bwav/studywright (wiki: 4 pages + sidebar, clone at Ai/studywright.wiki). Installed as studywright@studywright (local marketplace, user scope). Texas deck is "Texas Test Prep", 47 q (filibusters + Louisiana Purchase/Hidalgo guide); row 4 = Barr (Mark confirmed).

Banner merged 2026-11-10 (PR #1, seed 2313760545); Discussions on. Social preview (1280x640 centre crop) is UI-only: Mark uploads it in Settings when he likes.

0.3.0 (2026-11-10, session 4): persistent switchable hero with level-up feats/training, character sheet linking past games, paper trail (game saves JSON to Downloads; `sw.py records` files it into gitignored records/ with INDEX.md), follow-up deck natural-selection-2 for the son's 8 first-try misses (first run: 67%, recorded by hand from Mark's screenshot in records/natural-selection/).

0.4.0 (2026-11-10, session 5): realms (subject worlds, challenge text per question, 3D hero + obstacles), hero picker on Start quest; Texas game rebuilt for the next test. Biology test is over (Mark).

0.5.0 (2026-11-10, session 6): day-2 warm-up (last run's misses first) and read-aloud button.

Session 8: two-player hot-seat built; plugin bumped to 0.6.0 and released (see log).

Session 7: boss round (timed pass over first-try misses) merged; games rebuilt. Plugin.json not bumped or released since 0.2.0.

0.7.0 (2026-11-11, session 9): read lock, variants + steps, hero scenes with hp/gold/loot, hero builder with inventory; new deck natural-selection-3 for the son's next biology test (How Natural Selection Works to Key Takeaways). Older decks have no variants/steps yet.

2026-11-12: kickoff prompt written for lesson mode (teach, then test a method), a roguelike path map and a mean absolute deviation game for the son's HW 5.6 (due 2026-11-13); nothing built yet. Worksheet photo, transcription and answer key are in records/mean-absolute-deviation/ (gitignored).

0.8.0 (2026-11-12, session 11): world mode (open world, shared persistent land, keys and locked doors, signpost notes, sound, feel settings), templates/kit.js shared by all three templates (one hero drawing routine, builder with more options, notes prompt on every finish screen), lesson mode gained the hero picker and builder, deck selective-breeding ("Breeders' Valley", 45 q) for the biology test of 2026-11-13. Sheets and transcription in records/selective-breeding/ (gitignored). Mark's standing asks from this session: world mode is the main game; every play must leave a log and a notes prompt; heroes must look the same in every game.

Next:
00. When Mark pastes a notes prompt from a finish screen (or says the son played): `sw.py records`, update records/INDEX.md, this file and the log, and report what to review. Expected first: selective-breeding and mean-absolute-deviation.
01. Lesson mode still owes Mark's note of 2026-11-12: "needed a little more variation and explanation" (more contexts and question shapes per stage, a fuller worked explanation after a miss). Then the ludowright round from the kickoff prompt (ai-docs/plans/2026-11-12-lesson-mode-kickoff-prompt.md).
02. World mode ideas: `steps` after a miss, a shop for gold, feat picks on level-up inside the world, three.js or polywright art if Mark wants 3D (this build is a 2D canvas so it works offline from one file), convert texas-filibusters to a world deck so a second valley appears on the shared map.
0a. After the son plays natural-selection-3: `sw.py records`, report misses.
0b. Add variants/steps to texas-filibusters.
0. When the Texas game has been played: run `sw.py records`, read records/INDEX.md, report shaky ideas; consider per-question `scene` text for Texas.
1. Build ideas in skills/studywright/references/learning-design.md ("Ideas not built yet"), next: gear/titles for mastering a deck; release once a batch is in.
2. First everscout scan of beat learning-games; fold findings into RESEARCH.md.
3. evergreen-test evals for the skill (trigger + build case).
