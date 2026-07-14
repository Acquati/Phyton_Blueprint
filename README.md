# Phyton Blueprint

A Python project blueprint with a clean, modular structure designed for development by both humans and AI agents.

## Features

- **Domain-driven design** — clear separation of concerns across `core/`, `infrastructure/`, `app/`, `ui/`, `data/`, and `tools/`
- **Modern tooling** — ruff for linting and formatting, mypy for strict type checking, python -m pytest for testing
- **AI-friendly** — `AGENTS.md` and `prompts.md` guide AI agents through project conventions
- **Python 3.11+** — takes advantage of modern Python features

## Project Structure

```
src/
├── __init__.py       # Package version
├── app/              # Application entry points
├── core/             # Core business logic
├── data/             # Data models and schemas
├── infrastructure/   # External integrations (APIs, databases, files)
├── tools/            # Utility functions
└── ui/               # User interface
tests/                # Test suite
```

## Getting Started

### Prerequisites

- Python 3.11 or higher
- [hatch](https://hatch.pypa.io/) (recommended) or pip

### Install

```bash
# Using pip
pip install -e ".[dev]"

# Using hatch
hatch env create dev
```

### Run Tests

```bash
python -m pytest
```

### Lint and Format

```bash
ruff check
ruff format
```

### Type Check

```bash
mypy src
```

## Project Conventions

- Tab indentation (2 spaces wide)
- Strict type annotations on all functions
- No comments in code unless absolutely necessary
- Domain-driven design: business logic in `core/`, I/O in `infrastructure/`

See `AGENTS.md` for the full conventions guide used by AI agents.
