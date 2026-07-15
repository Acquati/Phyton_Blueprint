# AI Agent Guide

This file helps AI agents understand the project conventions when editing code.

## Project Structure

```
src/                    # Main source code
├── __init__.py         # Package version
├── app/                # Application entry points
├── core/               # Core business logic
├── data/               # Data models and schemas
├── infrastructure/     # External integrations
├── tools/              # Utility functions
└── ui/                 # User interface
tests/                  # Test suite
```

## Conventions

- Python 3.11+ required
- Use `ruff` for linting and formatting
- Use `mypy` for type checking (strict mode)
- Use `python -m pytest` for testing
- All functions must have type annotations
- Follow domain-driven design: core logic in `core/`, I/O in `infrastructure/`
- No comments in code unless absolutely necessary
- Tab indentation (2 spaces wide) per `.editorconfig`

## Commands

```bash
# Install with dev dependencies
pip install -e ".[dev]"
# or using hatch
hatch env create dev

# Run tests
python -m pytest

# Lint
python -m ruff check

# Format
python -m ruff format

# Type check
python -m mypy src
```

## Workflow

1. Understand the existing code before making changes
2. Follow the established patterns and conventions
3. Add tests for new functionality
4. Run lint + typecheck before finalizing
