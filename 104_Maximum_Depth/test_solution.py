"""Тесты для Maximum Depth of Binary Tree."""
import unittest
from solution import Solution, build_tree


class TestMaxDepth(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, values, expected):
        root = build_tree(values)
        result = self.sol.maxDepth(root)
        self.assertEqual(result, expected, f"tree={values}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check([3, 9, 20, None, None, 15, 7], 3)
    
    def test_example_2(self):
        self.check([1, None, 2], 2)
    
    # ---------- Граничные ----------
    def test_empty(self):
        self.check([], 0)
    
    def test_single(self):
        self.check([1], 1)
    
    def test_balanced(self):
        self.check([1, 2, 3, 4, 5, 6, 7], 3)
    
    # ---------- Вырожденные ----------
    def test_left_chain(self):
        self.check([1, 2, None, 3, None, 4], 4)
    
    def test_right_chain(self):
        self.check([1, None, 2, None, 3, None, 4], 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
