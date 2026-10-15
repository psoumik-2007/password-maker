# Security notes

## Randomness

Password Maker uses Python's `secrets` module rather than the simulation-
oriented `random` module. `secrets.choice` selects characters using the
operating system's cryptographically secure random source. The final
characters are shuffled with `secrets.SystemRandom`.

## Character groups and length

Difficulty 1 uses uppercase and lowercase ASCII letters. Difficulty 2 adds the
symbols `!@#$%^&*()-_=+[]{};:,.?/|~`. Difficulty 3 also adds digits `0`–`9`.
At least one character from each enabled group is included. Length must be at
least the number of enabled groups and may not exceed 4096.

The generator's output is written to standard output. Shell history, terminal
scrollback, logs, clipboard managers, or command pipelines may retain it.
Avoid redirecting generated passwords to files or services that are not
protected appropriately. Prefer a trusted password manager for storing
passwords.

## Limitations

This tool generates passwords locally and does not store, transmit, or manage
them. It does not assess the password policy of a particular website or
service. Follow the target service's requirements, and do not reuse passwords
between accounts.
