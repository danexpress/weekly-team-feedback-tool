## Commands

- `uv sync` - install dependencies
- `uv run pytest` - the whole suite
- `uv run pytest tests/test_home.py` - one test file
- `docker compose up -d` - start local Postgres (creates `app` and
  `app_test` databases)
- `uv run alembic upgrade head` - apply migrations to `DATABASE_URL`
  (defaults to the local `app` database)
- `uv run alembic downgrade base` - reverse all migrations
- `uv run alembic revision --autogenerate -m "message"` - generate a
  new migration from model changes
- `uv run python -m weekly_team_feedback_tool.seed` - seed sample
  users/project/memberships into `DATABASE_URL`
- Tests run against `TEST_DATABASE_URL` (defaults to the local
  `app_test` database) and create/drop their own schema

## Rules

- Dependencies are added in `pyproject.toml`. Do not add one without
  asking

## Workflow

- Tasks are GitHub issues, one at a time
- Read the acceptance criteria before starting and before closing
- Commit regularly

## Documents

- `_docs/process.md` - how work is organized
- Before writing tests, read `_docs/testing-guidelines.md`
- For anything touching the UI, read `_docs/design-system.md`
