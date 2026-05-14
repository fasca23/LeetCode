"""Тесты для Longest Substring Without Repeating Characters."""
import unittest
from solution import Solution


class TestLengthOfLongestSubstring(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, s, expected):
        result = self.sol.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected, f"s={s!r}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check("abcabcbb", 3)
    
    def test_example_2(self):
        self.check("bbbbb", 1)
    
    def test_example_3(self):
        self.check("pwwkew", 3)
    
    # ---------- Граничные ----------
    def test_empty(self):
        self.check("", 0)
    
    def test_single(self):
        self.check("a", 1)
    
    def test_spaces(self):
        self.check("a b c", 3)
    
    # ---------- Повторы ----------
    def test_all_unique(self):
        self.check("abcdef", 6)
    
    def test_repeat_at_end(self):
        self.check("abca", 3)
    
    def test_digits_and_symbols(self):
        self.check("a1!a1!", 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
