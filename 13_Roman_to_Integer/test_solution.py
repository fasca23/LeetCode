"""Тесты для Roman to Integer."""
import unittest
from solution import Solution


class TestRomanToInt(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, s, expected):
        result = self.sol.romanToInt(s)
        self.assertEqual(result, expected, f"s={s!r}")
    
    # ---------- Из условия ----------
    def test_simple_addition(self):
        self.check("III", 3)
    
    def test_with_subtraction(self):
        self.check("LVIII", 58)
    
    def test_complex(self):
        self.check("MCMXCIV", 1994)
    
    # ---------- Вычитание ----------
    def test_iv(self):
        self.check("IV", 4)
    
    def test_ix(self):
        self.check("IX", 9)
    
    def test_xl(self):
        self.check("XL", 40)
    
    def test_xc(self):
        self.check("XC", 90)
    
    def test_cd(self):
        self.check("CD", 400)
    
    def test_cm(self):
        self.check("CM", 900)
    
    # ---------- Граничные ----------
    def test_single(self):
        for ch, val in [('I', 1), ('V', 5), ('X', 10), ('L', 50),
                         ('C', 100), ('D', 500), ('M', 1000)]:
            self.check(ch, val)
    
    def test_max(self):
        self.check("MMMCMXCIX", 3999)


if __name__ == "__main__":
    unittest.main(verbosity=2)