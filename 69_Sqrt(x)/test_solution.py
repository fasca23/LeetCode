"""Тесты для Sqrt(x)."""
import unittest
from solution import Solution


class TestMySqrt(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, x, expected):
        result = self.sol.mySqrt(x)
        self.assertEqual(result, expected, f"x={x}")
    
    # ---------- Из условия ----------
    def test_perfect_square(self):
        self.check(4, 2)
    
    def test_rounded_down(self):
        self.check(8, 2)
    
    # ---------- Граничные ----------
    def test_zero(self):
        self.check(0, 0)
    
    def test_one(self):
        self.check(1, 1)
    
    def test_two(self):
        self.check(2, 1)
    
    # ---------- Обычные ----------
    def test_nine(self):
        self.check(9, 3)
    
    def test_ten(self):
        self.check(10, 3)
    
    def test_sixteen(self):
        self.check(16, 4)
    
    # ---------- Большие ----------
    def test_large(self):
        self.check(2147395599, 46339)
    
    def test_max(self):
        self.check(2**31 - 1, 46340)


if __name__ == "__main__":
    unittest.main(verbosity=2)
