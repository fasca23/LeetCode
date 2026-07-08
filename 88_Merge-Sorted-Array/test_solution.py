"""Тесты для Merge Sorted Array."""
import unittest
from solution import Solution


class TestMergeSortedArray(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, nums1, m, nums2, n, expected):
        original = nums1[:]
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected,
                         f"nums1={original}, m={m}, nums2={nums2}, n={n}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3,
                   [1, 2, 2, 3, 5, 6])
    
    def test_example_2(self):
        self.check([1], 1, [], 0, [1])
    
    def test_example_3(self):
        self.check([0], 0, [1], 1, [1])
    
    # ---------- Дополнительные ----------
    def test_all_nums2_smaller(self):
        self.check([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3,
                   [1, 2, 3, 4, 5, 6])
    
    def test_all_nums2_larger(self):
        self.check([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3,
                   [1, 2, 3, 4, 5, 6])
    
    def test_mixed(self):
        self.check([1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3,
                   [1, 2, 3, 4, 5, 6])
    
    def test_duplicates(self):
        self.check([1, 2, 2, 0, 0], 3, [1, 2], 2,
                   [1, 1, 2, 2, 2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
