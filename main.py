"""Generate cryptographically secure passwords from the command line."""

import argparse
import secrets
import string
from collections.abc import Sequence

LETTERS = string.ascii_letters
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/|~"
MAX_PASSWORD_LENGTH = 4096

CHARACTER_SETS = {
    1: (LETTERS,),
    2: (LETTERS, SYMBOLS),
    3: (LETTERS, SYMBOLS, DIGITS),
}


def generate_password(length: int = 16, difficulty: int = 3) -> str:
    """Generate a password with the selected character groups.

    Difficulty 1 uses letters, difficulty 2 adds symbols, and difficulty 3
    adds digits. Each selected group is guaranteed to appear at least once.
    """
    if not isinstance(length, int) or isinstance(length, bool):
        raise ValueError("length must be an integer")
    if not 1 <= length <= MAX_PASSWORD_LENGTH:
        raise ValueError(f"length must be between 1 and {MAX_PASSWORD_LENGTH}")
    if difficulty not in CHARACTER_SETS:
        raise ValueError("difficulty must be 1, 2, or 3")

    groups = CHARACTER_SETS[difficulty]
    if length < len(groups):
        raise ValueError(
            f"length must be at least {len(groups)} for difficulty {difficulty}"
        )

    password_characters = [secrets.choice(group) for group in groups]
    alphabet = "".join(groups)
    password_characters.extend(
        secrets.choice(alphabet) for _ in range(length - len(password_characters))
    )
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)


def _positive_integer(value: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be an integer") from exc
    if number < 1:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return number


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate cryptographically secure passwords."
    )
    parser.add_argument(
        "-l",
        "--length",
        type=_positive_integer,
        default=16,
        help=f"password length (1-{MAX_PASSWORD_LENGTH}; default: 16)",
    )
    parser.add_argument(
        "-d",
        "--difficulty",
        type=int,
        choices=sorted(CHARACTER_SETS),
        default=3,
        help="character groups: 1=letters, 2=letters and symbols, "
        "3=letters, symbols, and digits (default: 3)",
    )
    parser.add_argument(
        "-c",
        "--count",
        type=_positive_integer,
        default=1,
        help="number of passwords to generate (default: 1)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.length > MAX_PASSWORD_LENGTH:
        parser.error(f"--length must be no greater than {MAX_PASSWORD_LENGTH}")
    if args.length < len(CHARACTER_SETS[args.difficulty]):
        parser.error(
            f"--length must be at least {len(CHARACTER_SETS[args.difficulty])} "
            f"for difficulty {args.difficulty}"
        )

    for _ in range(args.count):
        print(generate_password(args.length, args.difficulty))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
