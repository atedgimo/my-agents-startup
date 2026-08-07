# Pulse 2026-08-07 20:34

**Trigger:** your card #0020 is in-progress  
**Dispatched to:** startup-backend-full-stack-devel

## Task

Card #0020 is yours: Feature: Implement Ghost Visual Identifiers & State Logic.

Make the change with ONE call to edit_code(card="0020", instruction="...") — describe the whole change in the instruction; it reads and edits the files itself and costs a fraction of doing it by hand. Reserve write_repo_file/edit_repo_file for docs and one-line tweaks. Then move the card to review with update_issue. If it is genuinely blocked, say exactly what blocks it and move it back to todo with a comment. One card this cycle, and do not create a new card instead of doing this one.

## Outcome

The ImportError persists despite moving ghost_ai.py content to ghosts.py on main branch.

The error traceback points to line 10 in the test file, which is the import of GhostIdentity and GhostState from src.backend.ghosts.

I suspect the problem is that the test file is importing GhostIdentity and GhostState from src.backend.ghosts but these classes are not defined or exported correctly in ghosts.py.

I will check the ghosts.py file to ensure GhostIdentity and GhostState are defined and accessible for import.

If needed, I will add explicit exports or fix naming to make them importable.
I have reviewed the ghosts.py content I wrote and it does define GhostIdentity and GhostState classes correctly.

The ImportError is likely due to the test file or pytest environment not recognizing the src/backend package correctly.

I have already added __init__.py to src/backend and tests/acceptance, and added src to sys.path in conftest.py.

The remaining possibility is that the test file name or folder name is invalid for pytest to import.

The test file is named test_ghost_visuals.py in tests/acceptance/ which is a valid pattern.

The error message hints "make sure your test modules/packages have valid Python names."

I will try renaming tests/acceptance/test_ghost_visuals.py to tests/acceptance/test_ghosts.py to match the module name ghosts.py.

This might help pytest import the test module correctly.

I will rename the test file and rerun acceptance.
