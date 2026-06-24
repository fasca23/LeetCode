"""Тесты для Longest Palindromic Substring."""
import unittest
from solution import Solution


class TestLongestPalindrome(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, s, expected):
        """expected — список допустимых ответов."""
        result = self.sol.longestPalindrome(s)
        self.assertIn(result, expected,
                      f"s={s!r}: получили {result!r}, ждали {expected}")
        # Проверяем что результат действительно палиндром
        self.assertEqual(result, result[::-1],
                         f"{result!r} не палиндром!")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check("babad", ["bab", "aba"])
    
    def test_example_2(self):
        self.check("cbbd", ["bb"])
    
    # ---------- Граничные ----------
    def test_single(self):
        self.check("a", ["a"])
    
    def test_all_same(self):
        self.check("aaaa", ["aaaa"])
    
    def test_no_palindrome(self):
        self.check("abc", ["a", "b", "c"])
    
    def test_full_string(self):
        self.check("racecar", ["racecar"])
    
    def test_even_palindrome(self):
        self.check("abba", ["abba"])


if __name__ == "__main__":
    unittest.main(verbosity=2)