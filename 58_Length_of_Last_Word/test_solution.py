"""Тесты для Length of Last Word."""
import unittest
from solution import Solution


class TestLengthOfLastWord(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, s, expected):
        result = self.sol.lengthOfLastWord(s)
        self.assertEqual(result, expected, f"s={s!r}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check("Hello World", 5)
    
    def test_example_2(self):
        self.check(" fly me to the moon ", 4)
    
    def test_example_3(self):
        self.check("luffy is still joyboy", 6)
    
    # ---------- Граничные ----------
    def test_single_word(self):
        self.check("a", 1)
    
    def test_only_spaces(self):
        self.check("   ", 0)
    
    def test_trailing_spaces(self):
        self.check("day   ", 3)
    
    def test_leading_spaces(self):
        self.check("   day", 3)
    
    def test_one_letter(self):
        self.check("x", 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
