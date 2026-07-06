"""Тесты для Reverse Integer."""
import unittest
from solution import Solution


class TestReverseInteger(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, x, expected):
        result = self.sol.reverse(x)
        self.assertEqual(result, expected, f"x={x}")
    
    # ---------- Из условия ----------
    def test_positive(self):
        self.check(123, 321)
    
    def test_negative(self):
        self.check(-123, -321)
    
    def test_trailing_zero(self):
        self.check(120, 21)
    
    # ---------- Граничные ----------
    def test_zero(self):
        self.check(0, 0)
    
    def test_single_digit(self):
        self.check(5, 5)
        self.check(-5, -5)
    
    # ---------- Переполнение ----------
    def test_overflow(self):
        self.check(1534236469, 0)
    
    def test_max_int(self):
        self.check(1463847412, 2147483641)
    
    def test_min_int(self):
        self.check(-1463847412, -2147483641)
    
    # ---------- Обычные ----------
    def test_palindrome(self):
        self.check(121, 121)
    
    def test_leading_zeros_result(self):
        self.check(100, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
