#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes a single word to /output/entry.txt.
Deterministic: the same word on every run, no network, no randomness.

The word is "irregardless": the word that should never have existed.
"Regardless" already does the whole job, so "irregardless" adds a
double negative and nothing else - a word dictionaries only list so
they can warn you not to use it. Deleting it costs the language
nothing and finally ends the argument. 12 characters, inside the
gate's 1-77 character limit.
"""

import os

WORD = "irregardless"


def main() -> None:
    # Gate check, same rule the sealed scorer applies: UTF-8 text of
    # 1 to 77 characters, not only white space. The entry is exactly
    # one word: no trailing newline, no extra whitespace, nothing
    # added around it.
    assert 1 <= len(WORD) <= 77 and WORD.strip(), "word fails the gate"
    assert WORD == WORD.strip() and " " not in WORD, "entry must be one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
