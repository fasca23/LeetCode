"""Тесты для Symmetric Tree."""
import unittest
from solution import Solution, build_tree


class TestSymmetricTree(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, values, expected):
        root = build_tree(values)
        result = self.sol.isSymmetric(root)
        self.assertEqual(result, expected, f"tree={values}")
    
    # ---------- Из условия ----------
    def test_symmetric(self):
        self.check([1, 2, 2, 3, 4, 4, 3], True)
    
    def test_not_symmetric(self):
        self.check([1, 2, 2, None, 3, None, 3], False)
    
    # ---------- Граничные ----------
    def test_empty(self):
        self.check([], True)
    
    def test_single(self):
        self.check([1], True)
    
    def test_two_nodes_same(self):
        self.check([1, 2, 2], True)
    
    def test_two_nodes_different(self):
        self.check([1, 2, 3], False)
    
    # ---------- Несимметричные ----------
    def test_asymmetric_structure(self):
        self.check([1, 2], False)
    
    def test_asymmetric_values(self):
        self.check([1, 2, 2, 3, 4, 5, 3], False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
