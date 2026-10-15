# Development guide

## Project layout

- `main.py` — password-generation function and command-line interface.
- `tests/test_main.py` — unit tests using the standard library `unittest`.
- `pyproject.toml` — Python project metadata and `password-maker` entry point.
- `requirements.txt` — runtime dependency list (currently no external packages).
- `docs/SECURITY.md` — randomness, output handling, and security limitations.

## Setup

Python 3.10 or newer is required. To install an editable copy and expose the
`password-maker` command:

```console
python -m pip install -e .
```

There are no third-party runtime dependencies. Editable installation uses
`setuptools` as the project build backend.

## Test

Run all unit tests from the repository root:

```console
python -m unittest discover -s tests -v
```

The tests use only Python's standard library and do not need network access.

## Public Python API

`generate_password(length=16, difficulty=3)` returns one password as a string.
It raises `ValueError` for unsupported difficulty levels, invalid lengths,
or lengths too short to include every required character group.

The command-line entry point accepts `--length`, `--difficulty`, and `--count`.
Run `python main.py --help` for the current option descriptions.
