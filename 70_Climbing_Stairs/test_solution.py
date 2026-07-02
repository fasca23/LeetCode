"""Тесты для Climbing Stairs."""
import unittest
from solution import Solution


class TestClimbStairs(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, n, expected):
        result = self.sol.climbStairs(n)
        self.assertEqual(result, expected, f"n={n}")
    
    # ---------- Из условия ----------
    def test_n2(self):
        self.check(2, 2)
    
    def test_n3(self):
        self.check(3, 3)
    
    # ---------- Граничные ----------
    def test_n1(self):
        self.check(1, 1)
    
    # ---------- Больше значений ----------
    def test_n4(self):
        self.check(4, 5)
    
    def test_n5(self):
        self.check(5, 8)
    
    def test_n6(self):
        self.check(6, 13)
    
    def test_n10(self):
        self.check(10, 89)
    
    def test_n45(self):
        # Максимальное значение по условию
        self.check(45, 1836311903)


if __name__ == "__main__":
    unittest.main(verbosity=2)
