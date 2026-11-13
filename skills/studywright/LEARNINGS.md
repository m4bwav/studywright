# Learnings

- Windows may refuse binding port 8765 (WinError 10013); serve games on 18765.
- Play-test cleanup (2026-11-12): a localStorage backup held in a `window` variable is lost on `location.reload()`; return the backup in the tool output or save it to sessionStorage before any reload, else restore has to be rebuilt by hand from the run's record.
- Play-test on a port never used before (2026-11-12: 18766): each origin has its own localStorage, so a fresh port cannot touch the heroes saved under file:// or an earlier test port, and `localStorage.clear()` afterwards is safe.
- Anything added to templates/kit.js runs inside verify_lesson.js's stub DOM too: guard canvas and window use, or the verifier fails before it checks a single item.
- World play-test from the console (2026-11-12): call `openQ(qi)` before `answer(qi, itemOf(qi), ok, given)`, since answer writes into the card openQ builds (TypeError on `#fb` otherwise), and enable `#nx` before clicking it to skip the read lock. Cleanup: the page's `pagehide` handler saves the run and the world again, so set `S=null` and call `localStorage.clear()` right before leaving; the world key may still be rewritten, which is harmless on a throwaway port.
