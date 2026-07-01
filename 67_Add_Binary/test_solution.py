"""Тесты для Add Binary."""
import unittest
from solution import Solution


class TestAddBinary(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, a, b, expected):
        result = self.sol.addBinary(a, b)
        self.assertEqual(result, expected, f"{a!r} + {b!r}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check("11", "1", "100")
    
    def test_example_2(self):
        self.check("1010", "1011", "10101")
    
    # ---------- Граничные ----------
    def test_zeros(self):
        self.check("0", "0", "0")
    
    def test_zero_plus_one(self):
        self.check("0", "1", "1")
    
    # ---------- Разная длина ----------
    def test_different_length(self):
        self.check("1", "111", "1000")
    
    def test_longer_first(self):
        self.check("101", "10", "111")
    
    # ---------- С переносом ----------
    def test_all_ones(self):
        self.check("111", "111", "1110")
    
    def test_carry_chain(self):
        self.check("1111", "1", "10000")


if __name__ == "__main__":
    unittest.main(verbosity=2)
