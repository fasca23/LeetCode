"""Тесты для Remove Duplicates from Sorted List."""
import unittest
from solution import Solution, to_linked, to_list


class TestDeleteDuplicates(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, arr, expected):
        head = to_linked(arr)
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(to_list(result), expected, f"input={arr}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check([1, 1, 2], [1, 2])
    
    def test_example_2(self):
        self.check([1, 1, 2, 3, 3], [1, 2, 3])
    
    # ---------- Граничные ----------
    def test_empty(self):
        self.check([], [])
    
    def test_single(self):
        self.check([1], [1])
    
    def test_all_duplicates(self):
        self.check([1, 1, 1], [1])
    
    def test_no_duplicates(self):
        self.check([1, 2, 3], [1, 2, 3])
    
    def test_two_nodes_same(self):
        self.check([2, 2], [2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
