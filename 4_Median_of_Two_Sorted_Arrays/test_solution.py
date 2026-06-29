"""Тесты для Median of Two Sorted Arrays."""
import unittest
from solution import Solution


class TestFindMedianSortedArrays(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, nums1, nums2, expected):
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected,
                         f"nums1={nums1}, nums2={nums2}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check([1, 3], [2], 2.0)
    
    def test_example_2(self):
        self.check([1, 2], [3, 4], 2.5)
    
    # ---------- Граничные ----------
    def test_one_empty(self):
        self.check([], [1], 1.0)
        self.check([2], [], 2.0)
    
    def test_both_empty(self):
        # По условию такого нет, но для полноты
        pass
    
    def test_different_size(self):
        self.check([1, 3, 8], [7, 9, 10, 11], 8.0)
    
    def test_even_total(self):
        self.check([1, 2], [3, 4], 2.5)
    
    def test_odd_total(self):
        self.check([1, 3, 5], [2, 4], 3.0)
    
    def test_negative(self):
        self.check([-5, -3], [-2, -1], -2.5)
    
    def test_same_elements(self):
        self.check([1, 1], [1, 1], 1.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
