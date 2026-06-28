"""Тесты для Plus One."""
import unittest
from solution import Solution


class TestPlusOne(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, digits, expected):
        result = self.sol.plusOne(digits[:])
        self.assertEqual(result, expected, f"digits={digits}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check([1, 2, 3], [1, 2, 4])
    
    def test_example_2(self):
        self.check([4, 3, 2, 1], [4, 3, 2, 2])
    
    def test_example_3(self):
        self.check([9], [1, 0])
    
    # ---------- Граничные ----------
    def test_all_nines(self):
        self.check([9, 9, 9], [1, 0, 0, 0])
    
    def test_zero(self):
        self.check([0], [1])
    
    def test_no_carry(self):
        self.check([1, 2, 4], [1, 2, 5])
    
    def test_carry_middle(self):
        self.check([1, 9, 9], [2, 0, 0])
    
    def test_single_digit(self):
        self.check([5], [6])


if __name__ == "__main__":
    unittest.main(verbosity=2)
