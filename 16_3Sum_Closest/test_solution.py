"""Тесты для 3Sum Closest."""
import unittest
from solution import Solution


class TestThreeSumClosest(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, nums, target, expected):
        result = self.sol.threeSumClosest(nums, target)
        self.assertEqual(result, expected,
                         f"nums={nums}, target={target}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check([-1, 2, 1, -4], 1, 2)
    
    def test_example_2(self):
        self.check([0, 0, 0], 1, 0)
    
    # ---------- Граничные ----------
    def test_exact_match(self):
        self.check([1, 1, 1, 0], -100, 2)
    
    def test_negative_target(self):
        self.check([4, 0, 5, -5, 3, 3], -1, -1)
    
    def test_minimal(self):
        self.check([1, 1, 1], 3, 3)
    
    def test_all_same(self):
        self.check([2, 2, 2, 2], 7, 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
