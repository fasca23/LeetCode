"""Тесты для Same Tree (DFS со стеком)."""
import unittest
from solution import Solution, build_tree


class TestSameTree(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, p_vals, q_vals, expected):
        p = build_tree(p_vals)
        q = build_tree(q_vals)
        result = self.sol.isSameTree(p, q)
        self.assertEqual(result, expected,
                         f"p={p_vals}, q={q_vals}")
    
    # ---------- Из условия ----------
    def test_same(self):
        self.check([1, 2, 3], [1, 2, 3], True)
    
    def test_different_structure(self):
        self.check([1, 2], [1, None, 2], False)
    
    def test_different_values(self):
        self.check([1, 2, 1], [1, 1, 2], False)
    
    # ---------- Граничные ----------
    def test_both_empty(self):
        self.check([], [], True)
    
    def test_one_empty(self):
        self.check([1], [], False)
    
    def test_single_node(self):
        self.check([0], [0], True)
        self.check([0], [1], False)
    
    # ---------- Вырожденное (цепочка) ----------
    def test_chain_same(self):
        # 100 узлов в цепочку — без рекурсии не упадёт
        p_vals = list(range(100))
        q_vals = list(range(100))
        self.check(p_vals, q_vals, True)
    
    def test_chain_different(self):
        p_vals = list(range(100))
        q_vals = list(range(99)) + [999]
        self.check(p_vals, q_vals, False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
