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

Merged as PR #9, released v0.8.0, installed plugin updated to 0.8.0 (2026-11-12). The wiki still describes 0.2.0 to 0.6.0: world mode, lesson mode and the kit are not on it yet.

0.9.0 (2026-11-12, session 12): world deck texas-independence ("Texas Frontier", 90 q, 8 regions) for the Texas history test of 2026-11-13, from the six-page study guide "Mexican Independence, Filibusters & Empresarios" plus a review region from texas-filibusters. Engine: `order` questions, SVG pictures with a lit shape, and a placement fix (a creature could be walled in). It appears as a second valley on the shared land. Sheet reading notes and what the son got wrong are in records/texas-independence/study-guide-notes.md (gitignored). Samuel Kemper is left out of the game: the son wrote NO, history says filibuster, and the class key is unknown. The wiki still describes 0.2.0 to 0.6.0.

2026-11-12 (session 13): first Breeders' Valley play filed (records/selective-breeding/2026-11-13-03-16.md, written by hand from the pasted notes prompt because the log was not in Downloads). 80% first try (36/45), all 45 mastered, 29 min, every signpost read except the mill (four steps). Nine first-try misses, all right on the retry. Shaky ideas, most to least:
- trait / gene / variation get swapped (typed "traits" for genes and "trait" for variation; chose "makes more genetic variation every time"). Variation was also missed on 2026-11-10 in natural-selection, so it is a repeat across two games.
- the downside of selective breeding (chose "always makes animals healthier"; the sheet says similar genes, less variation, disease hits all, health problems passed on).
- step 2 (choose parents) against step 3 (choose the best offspring): typed "best" for step 2.
- the sheet's exact blank words: naturally, more milk, large eggs (idea right on the reworded retry; matters only if the test is fill-in-the-blank).
- Baby Z parents: picked speed for "lift a car"; likely a reading slip.
A follow-up deck (`"follows": "selective-breeding"`) should re-test each of these twice in new scenarios: sort statements into gene / trait / variation; a one-disease crop field and a dog breed with a health problem (what happened to variation?); an `order` question for the four steps with a new organism plus "which step is this?"; one typed blank each in the sheet's wording; one more parents-of-baby item with a close distractor. The test is 2026-11-13, so build it only if Mark asks tonight or the unit continues.

Fixed in the same session: `sw.py records` crashed while rebuilding INDEX.md on any other JSON in records/ (banned-sets.json is a list); it now skips files that are not records. Not released; the fix is on main only.

Open question: no studywright-*.json was in C:\Users\m4bwa\Downloads after this play. Either the browser saves elsewhere or the world finish screen did not download; check on the next play (the session 11 test saw the download in Chrome).

0.10.0 (2026-11-12, session 14): merchants in world mode, asked by Mark before the son plays Texas Frontier. A region with `merchant` gets a trader placed after the creatures (no creature moves). Stock: healing potion 10 gold (drunk by itself at zero hearts), trail map 25 (clears the valley fog), compass 40 (HUD arrow to the nearest waiting creature, kept on the hero); deck keepsakes 20 each that show a fact from the notes. Texas Frontier has a merchant in all 8 regions and 15 keepsakes; the ones in bigpic and clock repeat what the son got wrong on the sheet (who gained what after the Seven Years' War, the 11 years). The record now has `bought` and `gold`. selective-breeding has no merchants (its deck has no `merchant` keys). The wiki still describes 0.2.0 to 0.6.0.

Merged as PR #12, released v0.10.0, installed plugin updated to 0.10.0 (2026-11-12; restart the editor to load it). Not yet played by the son: the built game is games/texas-independence.html.

Next:
00a. When the Texas Frontier log or notes prompt arrives: `sw.py records`, report misses. Ask what the class key says for Samuel Kemper and add him to the deck.
00. When Mark pastes a notes prompt from a finish screen (or says the son played): `sw.py records`, update records/INDEX.md, this file and the log, and report what to review. selective-breeding arrived 2026-11-12 (above); still expected: mean-absolute-deviation and texas-independence. If the log file is missing from Downloads again, find out why before writing the record by hand.
01. Lesson mode still owes Mark's note of 2026-11-12: "needed a little more variation and explanation" (more contexts and question shapes per stage, a fuller worked explanation after a miss). Then the ludowright round from the kickoff prompt (ai-docs/plans/2026-11-12-lesson-mode-kickoff-prompt.md).
02. Update the wiki (clone at Ai/studywright.wiki) for 0.8.0.
03. World mode ideas: `steps` after a miss, more merchant goods (hero cosmetics for gold), merchants for selective-breeding if it is played again, feat picks on level-up inside the world, three.js or polywright art if Mark wants 3D (this build is a 2D canvas so it works offline from one file), convert texas-filibusters to a world deck so a second valley appears on the shared map.
0a. After the son plays natural-selection-3: `sw.py records`, report misses.
0b. Add variants/steps to texas-filibusters.
0. When the Texas game has been played: run `sw.py records`, read records/INDEX.md, report shaky ideas; consider per-question `scene` text for Texas.
1. Build ideas in skills/studywright/references/learning-design.md ("Ideas not built yet"), next: gear/titles for mastering a deck; release once a batch is in.
2. First everscout scan of beat learning-games; fold findings into RESEARCH.md.
3. evergreen-test evals for the skill (trigger + build case).
