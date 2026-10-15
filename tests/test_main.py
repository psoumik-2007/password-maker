import contextlib
import io
import string
import unittest

from main import CHARACTER_SETS, SYMBOLS, build_parser, generate_password, main


class GeneratePasswordTests(unittest.TestCase):
    def test_password_has_requested_length_and_enabled_groups(self):
        for difficulty, groups in CHARACTER_SETS.items():
            length = max(12, len(groups))
            password = generate_password(length, difficulty)
            self.assertEqual(len(password), length)
            for group in groups:
                self.assertTrue(any(character in group for character in password))

    def test_difficulty_one_uses_only_letters(self):
        password = generate_password(64, 1)
        self.assertTrue(all(character in string.ascii_letters for character in password))

    def test_difficulty_two_uses_no_digits(self):
        password = generate_password(64, 2)
        self.assertTrue(all(character not in string.digits for character in password))
        self.assertTrue(any(character in SYMBOLS for character in password))

    def test_rejects_invalid_length_and_difficulty(self):
        for length, difficulty in ((0, 1), (4097, 1), (1, 2), (2, 3), (10, 4)):
            with self.subTest(length=length, difficulty=difficulty):
                with self.assertRaises(ValueError):
                    generate_password(length, difficulty)

    def test_rejects_non_integer_length(self):
        with self.assertRaises(ValueError):
            generate_password("12", 1)


class CommandLineTests(unittest.TestCase):
    def test_count_prints_one_password_per_line(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exit_code = main(["--length", "12", "--difficulty", "3", "--count", "4"])
        self.assertEqual(exit_code, 0)
        lines = output.getvalue().splitlines()
        self.assertEqual(len(lines), 4)
        self.assertTrue(all(len(password) == 12 for password in lines))

    def test_parser_defaults(self):
        args = build_parser().parse_args([])
        self.assertEqual((args.length, args.difficulty, args.count), (16, 3, 1))

    def test_rejects_nonpositive_count(self):
        with self.assertRaises(SystemExit):
            main(["--count", "0"])


if __name__ == "__main__":
    unittest.main()
