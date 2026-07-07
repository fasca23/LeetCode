"""Тесты для Regular Expression Matching."""
import unittest
from solution import Solution


class TestIsMatch(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, s, p, expected):
        result = self.sol.isMatch(s, p)
        self.assertEqual(result, expected, f"s={s!r}, p={p!r}")
    
    # ---------- Из условия ----------
    def test_no_star_fail(self):
        self.check("aa", "a", False)
    
    def test_star(self):
        self.check("aa", "a*", True)
    
    def test_dot_star(self):
        self.check("ab", ".*", True)
    
    # ---------- Составные шаблоны ----------
    def test_c_star(self):
        self.check("aab", "c*a*b", True)
    
    def test_mississippi(self):
        self.check("mississippi", "mis*is*p*.", False)
    
    # ---------- Граничные ----------
    def test_empty_both(self):
        self.check("", "", True)
    
    def test_empty_s(self):
        self.check("", ".*", True)
    
    def test_empty_s_pattern(self):
        self.check("", "a*", True)
    
    def test_empty_s_no_star(self):
        self.check("", "a", False)
    
    # ---------- Точка ----------
    def test_dot(self):
        self.check("abc", "a.c", True)
        self.check("abc", "a.d", False)
    
    # ---------- Звёздочка ----------
    def test_star_zero(self):
        self.check("b", "a*b", True)
    
    def test_star_many(self):
        self.check("aaab", "a*b", True)
    
    def test_multiple_stars(self):
        self.check("aaa", "a*a", True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
