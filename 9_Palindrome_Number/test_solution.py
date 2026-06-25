"""Тесты для Palindrome Number."""
import unittest
from solution import Solution


class TestPalindromeNumber(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, x, expected):
        result = self.sol.isPalindrome(x)
        self.assertEqual(result, expected, f"x={x}")
    
    # ---------- Из условия ----------
    def test_palindrome(self):
        self.check(121, True)
    
    def test_negative(self):
        self.check(-121, False)
    
    def test_not_palindrome(self):
        self.check(10, False)
    
    # ---------- Граничные ----------
    def test_zero(self):
        self.check(0, True)
    
    def test_single_digit(self):
        for i in range(10):
            self.check(i, True)
    
    def test_ends_with_zero(self):
        self.check(100, False)
    
    # ---------- Чётные/нечётные ----------
    def test_even_digits(self):
        self.check(1221, True)
        self.check(1234, False)
    
    def test_odd_digits(self):
        self.check(12321, True)
        self.check(12345, False)


if __name__ == "__main__":
    unittest.main(verbosity=2)