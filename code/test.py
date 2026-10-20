import unittest

from scrabble import scrabble_score


class TestScrabbleScore(unittest.TestCase):
    def test_example_cabbage(self):
        self.assertEqual(scrabble_score("cabbage"), 14)

    def test_empty_string(self):
        self.assertEqual(scrabble_score(""), 0)

    def test_single_letter_each_value_group(self):
        cases = {"a": 1, "d": 2, "b": 3, "f": 4, "k": 5, "j": 8, "q": 10}
        for letter, expected in cases.items():
            with self.subTest(letter=letter):
                self.assertEqual(scrabble_score(letter), expected)

    def test_every_letter_value(self):
        expected = {
            **dict.fromkeys("AEIOULNRST", 1),
            **dict.fromkeys("DG", 2),
            **dict.fromkeys("BCMP", 3),
            **dict.fromkeys("FHVWY", 4),
            "K": 5,
            **dict.fromkeys("JX", 8),
            **dict.fromkeys("QZ", 10),
        }
        self.assertEqual(len(expected), 26)
        for letter, value in expected.items():
            with self.subTest(letter=letter):
                self.assertEqual(scrabble_score(letter), value)

    def test_whole_alphabet(self):
        self.assertEqual(scrabble_score("abcdefghijklmnopqrstuvwxyz"), 87)

    def test_case_insensitive(self):
        self.assertEqual(scrabble_score("CABBAGE"), 14)
        self.assertEqual(scrabble_score("CaBbAgE"), 14)
        self.assertEqual(scrabble_score("Quiz"), scrabble_score("qUIZ"))

    def test_ignores_non_alphabetic(self):
        self.assertEqual(scrabble_score("cab-bage!"), 14)
        self.assertEqual(scrabble_score("  cabbage  "), 14)
        self.assertEqual(scrabble_score("c4bb4ge"), 12)  # a's replaced by digits
        self.assertEqual(scrabble_score("123 !@#"), 0)

    def test_ignores_non_english_letters(self):
        self.assertEqual(scrabble_score("café"), 8)  # é ignored: c3 a1 f4

    def test_longer_words(self):
        self.assertEqual(scrabble_score("street"), 6)
        self.assertEqual(scrabble_score("quirky"), 22)
        self.assertEqual(scrabble_score("OxyphenButazone"), 41)

    def test_non_string_raises(self):
        with self.assertRaises(TypeError):
            scrabble_score(None)
        with self.assertRaises(TypeError):
            scrabble_score(42)


if __name__ == "__main__":
    unittest.main()
