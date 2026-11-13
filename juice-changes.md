# Juice changes

## 2026-11-12 world mode (skills/studywright/templates/world.html), built with its feel from the start

Settings object `J` (stored in `studywright:settings`, gear menu in the HUD): `sound`, `shakeScale` (0, 0.5, 1), `reduceMotion` (defaults to the system setting), `flashes`, `hitStop`. With everything off the game plays the same; no rule reads these.

| Effect | Where | Constants (top of the script) | Gate |
|---|---|---|---|
| Trauma screen shake on a bump, a locked door and a miss | `shake()` in `bump`, `move`, `answer` | SHAKE_BUMP .18, SHAKE_MISS .65, SHAKE_MAX_PX 9, SHAKE_DECAY 2.4 | shakeScale, reduceMotion |
| Hit pause when a right answer lands | `answer` | HITSTOP_MS 70 | hitStop, reduceMotion |
| Particle bursts (build, key, door, chest, level, finish), capped | `burst()` | PARTICLES_MAX 140, BURST_N 24 | a quarter of the count under reduceMotion |
| Build pop (scale overshoot) on a mastered site | `pops` in `drawTile` | POP_MS 450 | none (one-off scale) |
| Hero hop and squash on each step, idle bob, creature bob, water shimmer | `frame`, `drawHero`, `drawTile` | HOP_PX 6, SQUASH .14 | reduceMotion |
| Floating +XP and +gold text | `floatText()` | - | none |
| One red edge flash on a miss | `flash()` | FLASH_MS 260 | flashes |
| Synth sound with pitch variation (step, bump, right, wrong, coin, key, door, locked, sign, discover, build, chest, faint, level, win) | `Sound` | PITCH_VAR .07, VOLUME .14 | sound |

Revert: turn the setting off in the gear menu, or set the constant to 0. Tune first: SHAKE_MISS and MOVE_MS (walk speed, a rule constant, 125 ms per tile).
