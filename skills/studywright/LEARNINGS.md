# Learnings

- Windows may refuse binding port 8765 (WinError 10013); serve games on 18765.
- Play-test cleanup (2026-11-12): a localStorage backup held in a `window` variable is lost on `location.reload()`; return the backup in the tool output or save it to sessionStorage before any reload, else restore has to be rebuilt by hand from the run's record.
