# How Work Is Organized

## Source of truth

Work is tracked as GitHub issues, one per task from `_docs/tasks.md`. If
the scope of a task changes, update the issue first — `_docs/tasks.md`
should stay in sync with it, not the other way around.

## Picking up a task

1. Pick a single open issue. Don't start a second one before the first
   is closed.
2. Read the whole issue — Goal, Description, and Acceptance Criteria —
   before writing any code. If the acceptance criteria are unclear or
   missing, ask before starting rather than guessing.
3. Create a branch named `issue-<number>-<short-slug>`, e.g.
   `issue-8-feedback-card-submission`.

## While working

- Commit regularly, in small logical steps, not one commit at the end.
- Each commit message should be a plain-English description of what
  changed and why; reference the issue number (`#8`) where useful.
- Re-read the acceptance criteria before opening a PR and before
  closing the issue — confirm each bullet is actually satisfied, not
  just "probably fine."
- Run the relevant tests locally before pushing (see
  `_docs/testing-guidelines.md`).

## Opening a pull request

- One issue per PR. If you find unrelated work while in there, note it
  as a new issue instead of expanding the PR's scope.
- The PR description should link the issue (`Closes #8`) and briefly
  state what changed.
- The PR should be small enough to review in one sitting — if it isn't,
  the underlying issue was probably too big and should have been split.

## Closing out

- An issue is only closed once its acceptance criteria are verified,
  not just once code is merged.
- If a task turns out to depend on work that hasn't landed yet, say so
  on the issue and pick a different one rather than half-implementing
  around the gap.
