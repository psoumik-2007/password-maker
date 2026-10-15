# Password Maker

Password Maker is a small command-line tool for generating random passwords
using Python's cryptographically secure `secrets` module. Choose a password
length, character-set difficulty, and number of passwords to generate.

## Features

- Uses the operating system's secure randomness through Python's `secrets`
  module.
- Guarantees at least one character from every character group enabled by the
  selected difficulty.
- Supports generating multiple passwords in one command.
- Uses only the Python standard library at runtime; no third-party runtime
  packages are required.

## Requirements

- Python 3.10 or newer.
- No third-party runtime dependencies.

The `requirements.txt` file is intentionally empty apart from explanatory
comments because all runtime imports are from the Python standard library.
Project metadata and the installable command are defined in `pyproject.toml`.

## Quick start

Run directly from the project directory:

```console
python main.py
```

This generates one 16-character password using letters, symbols, and digits.

### Command-line options

| Option | Default | Description |
| --- | ---: | --- |
| `-l`, `--length` | `16` | Password length, from 1 through 4096. |
| `-d`, `--difficulty` | `3` | Character groups to include; see below. |
| `-c`, `--count` | `1` | Number of passwords to generate. |
| `-h`, `--help` | — | Show usage and exit. |

Difficulty levels:

| Level | Character groups | Minimum length |
| ---: | --- | ---: |
| `1` | Uppercase and lowercase letters | 1 |
| `2` | Letters and symbols | 2 |
| `3` | Letters, symbols, and digits | 3 |

Every enabled group is represented at least once. The remaining characters are
selected from the combined enabled groups, and the result is securely
shuffled.

Examples:

```console
python main.py --length 24 --difficulty 3
python main.py -l 12 -d 2 --count 5
python main.py --help
```

The second example prints five separate 12-character passwords, one per line.
Invalid arguments (including a length shorter than the selected difficulty
requires) are reported with a usage message.

## Install as a command

With Python and `pip` available, install the project in editable mode:

```console
python -m pip install -e .
password-maker --length 24 --difficulty 3
```

The editable install uses the build backend declared in `pyproject.toml`.
Installing the project does not add third-party runtime dependencies.

## Development

Run the unit tests with Python's built-in test runner:

```console
python -m unittest discover -s tests -v
```

See [Development guide](docs/DEVELOPMENT.md) for project structure and
contribution checks, and [Security notes](docs/SECURITY.md) for guidance on
password generation and handling.

## License

No license has been specified yet. All rights and permissions are reserved by
the copyright holder unless a license is added to this repository.
