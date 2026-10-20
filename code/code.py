"""Simple Scrabble scoring for English words."""

LETTER_VALUES = {}
for letters, value in [
    ("AEIOULNRST", 1),
    ("DG", 2),
    ("BCMP", 3),
    ("FHVWY", 4),
    ("K", 5),
    ("JX", 8),
    ("QZ", 10),
]:
    for letter in letters:
        LETTER_VALUES[letter] = value


def scrabble_score(word):
    """Return the Scrabble score of `word`.

    Case-insensitive; non-alphabetic characters (digits, spaces,
    punctuation, accented/non-English letters) are ignored.
    """
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    return sum(LETTER_VALUES.get(ch, 0) for ch in word.upper())


if __name__ == "__main__":
    import sys

    words = sys.argv[1:] or [input("Enter a word: ")]
    for w in words:
        print(f"{w}: {scrabble_score(w)}")
