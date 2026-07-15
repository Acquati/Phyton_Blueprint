# AI Prompts

This file contains prompts and instructions for AI agents working on this project.

## Before Making Changes

1. Read `AGENTS.md` to understand project conventions
2. Read `README.md` for project overview
3. Examine existing code in the relevant module to match patterns and style
4. Check `pyproject.toml` for tool configurations (ruff, mypy, pytest)

## Code Generation Rules

- All functions must include type annotations
- Use `pathlib.Path` over `os.path`
- Prefer `Exception` subclasses over bare `except` clauses
- Return early rather than nesting deeply
- Use domain-driven design: business rules belong in `core/`, I/O belongs in `infrastructure/`

## Verification

After making changes, always run:

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy src
python -m pytest
```
