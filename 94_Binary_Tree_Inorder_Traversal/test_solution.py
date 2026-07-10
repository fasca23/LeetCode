"""Тесты для Binary Tree Inorder Traversal."""
import unittest
from solution import Solution, build_tree


class TestInorderTraversal(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, values, expected):
        root = build_tree(values)
        result = self.sol.inorderTraversal(root)
        self.assertEqual(result, expected, f"tree={values}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check([1, None, 2, 3], [1, 3, 2])
    
    def test_empty(self):
        self.check([], [])
    
    def test_single(self):
        self.check([1], [1])
    
    # ---------- Дополнительные ----------
    def test_full_tree(self):
        self.check([1, 2, 3, 4, 5], [4, 2, 5, 1, 3])
    
    def test_left_skewed(self):
        self.check([1, 2, None, 3], [3, 2, 1])
    
    def test_right_skewed(self):
        self.check([1, None, 2, None, 3], [1, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
