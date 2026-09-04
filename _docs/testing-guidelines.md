# Testing Guidelines

## Running tests

- `uv run pytest` runs the whole suite.
- `uv run pytest tests/test_home.py` runs a single file while you work
  on one area.
- The full suite must pass before a PR is opened, not just the file you
  touched.

## Where tests live

- Tests live under `tests/`, mirroring the structure of the code they
  cover (e.g. code in `app/feedback/` is tested from
  `tests/feedback/` or `tests/test_feedback.py`).
- Name test files `test_<thing>.py` and test functions
  `test_<behavior being verified>`, not `test_1`, `test_case_a`, etc.
  The name should make it possible to tell what broke from the test
  name alone.

## What to test

- Test the behavior described in the issue's acceptance criteria, not
  implementation details. If the acceptance criteria say "a
  non-facilitator cannot reveal a cycle," write a test that asserts
  exactly that, rather than testing internal helper functions in
  isolation.
- Every new endpoint or user-visible behavior needs at least one test
  covering the expected case and one covering the main failure/edge
  case (e.g. permission denied, validation error, boundary condition).
- Prefer a few focused tests over one large test asserting many things
  — a failure should point at a specific behavior.

## Test independence

- Tests must not depend on execution order or on state left behind by
  another test. Use fixtures to set up and tear down data for each
  test.
- Don't rely on a shared/dev database with pre-existing data. Each test
  should create the data it needs.

## Isolating external services

The app calls out to several external services — the LLM API, a
transcription API, object storage, and (later) email. Tests must not
make real network calls to any of these:

- Mock or stub these calls in unit and integration tests.
- If a test genuinely needs to exercise the real integration, mark it
  clearly (e.g. a separate `tests/integration/` or a marker) and keep
  it out of the default `uv run pytest` run so the suite stays fast and
  deterministic.

## Before closing an issue

Re-run the full suite (`uv run pytest`), not just the tests you added,
and confirm it's green before marking the issue's acceptance criteria
as met.
