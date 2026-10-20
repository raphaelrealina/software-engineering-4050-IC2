import unittest

from scrabble import scrabble_score


class TestScrabbleScore(unittest.TestCase):
    #Use cabbage test case on sheet, should return 14. -> raf
    def test_example_cabbage(self):
        self.assertEqual(scrabble_score("cabbage"), 14)

    #Teest to see if string is empty. -> sky
    def test_empty_string(self):
        self.assertEqual(scrabble_score(""), 0)

    #Checks one representative letter from each point-value group. -> raf
    def test_single_letter_each_value_group(self):
        cases = {"a": 1, "d": 2, "b": 3, "f": 4, "k": 5, "j": 8, "q": 10}
        for letter, expected in cases.items():
            with self.subTest(letter=letter):
                self.assertEqual(scrabble_score(letter), expected)   

    #Checks that the full alphabet scores 87 in total -> raf
    def test_whole_alphabet(self):
        self.assertEqual(scrabble_score("abcdefghijklmnopqrstuvwxyz"), 87)

    #Checks that uppercase, mixed-case, and lowercase versions of a word all score the same -> sky
    def test_case_insensitive(self):
        self.assertEqual(scrabble_score("CABBAGE"), 14)
        self.assertEqual(scrabble_score("CaBbAgE"), 14)
        self.assertEqual(scrabble_score("Quiz"), scrabble_score("qUIZ"))

    #checks that only letters contribute to the score.ß - sky
    def test_ignores_non_alphabetic(self):
        self.assertEqual(scrabble_score("cab-bage!"), 14)
        self.assertEqual(scrabble_score("  cabbage  "), 14)
        self.assertEqual(scrabble_score("c4bb4ge"), 12)  # a's replaced by digits
        self.assertEqual(scrabble_score("123 !@#"), 0)

if __name__ == "__main__":
    unittest.main()
