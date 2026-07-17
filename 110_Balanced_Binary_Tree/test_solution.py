"""Тесты для Balanced Binary Tree."""
import unittest
from solution import Solution, build_tree


class TestBalancedTree(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, values, expected):
        root = build_tree(values)
        result = self.sol.isBalanced(root)
        self.assertEqual(result, expected, f"tree={values}")
    
    # ---------- Из условия ----------
    def test_balanced(self):
        self.check([3, 9, 20, None, None, 15, 7], True)
    
    def test_not_balanced(self):
        self.check([1, 2, 2, 3, 3, None, None, 4, 4], False)
    
    # ---------- Граничные ----------
    def test_empty(self):
        self.check([], True)
    
    def test_single(self):
        self.check([1], True)
    
    def test_two_nodes(self):
        self.check([1, 2], True)
    
    # ---------- Вырожденные ----------
    def test_left_chain(self):
        self.check([1, 2, None, 3], False)
    
    def test_right_chain(self):
        self.check([1, None, 2, None, 3], False)
    
    # ---------- Сбалансированное ----------
    def test_perfect_tree(self):
        self.check([1, 2, 3, 4, 5, 6, 7], True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
