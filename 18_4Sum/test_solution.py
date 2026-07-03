"""Тесты для 4Sum."""
import unittest
from solution import Solution


class TestFourSum(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, nums, target, expected):
        result = self.sol.fourSum(nums, target)
        result_sorted = sorted([sorted(q) for q in result])
        expected_sorted = sorted([sorted(q) for q in expected])
        self.assertEqual(result_sorted, expected_sorted,
                         f"nums={nums}, target={target}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check([1, 0, -1, 0, -2, 2], 0,
                   [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
    
    def test_example_2(self):
        self.check([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]])
    
    # ---------- Граничные ----------
    def test_less_than_4(self):
        self.check([1, 2, 3], 6, [])
    
    def test_all_zeros(self):
        self.check([0, 0, 0, 0], 0, [[0, 0, 0, 0]])
    
    def test_negative(self):
        self.check([-1, 0, 1, 2, -1, -4], -1, [[-4, 0, 1, 2], [-1, -1, 0, 1]])
    
    # ---------- Ранний выход ----------
    def test_no_solution(self):
        self.check([1, 2, 3, 4], 100, [])
    
    def test_large_numbers(self):
        self.check([1000000000, 1000000000, 1000000000, 1000000000],
                   -294967296, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
