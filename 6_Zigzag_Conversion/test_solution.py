"""Тесты для Zigzag Conversion."""
import unittest
from solution import Solution


class TestZigzagConversion(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, s, numRows, expected):
        result = self.sol.convert(s, numRows)
        self.assertEqual(result, expected,
                         f"s={s!r}, rows={numRows}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR")
    
    def test_example_2(self):
        self.check("PAYPALISHIRING", 4, "PINALSIGYAHRPI")
    
    def test_single_row(self):
        self.check("A", 1, "A")
    
    # ---------- Граничные ----------
    def test_rows_more_than_length(self):
        self.check("AB", 5, "AB")
    
    def test_two_rows(self):
        self.check("ABCD", 2, "ACBD")
    
    def test_three_rows_short(self):
        self.check("ABC", 3, "ABC")
    
    def test_empty(self):
        self.check("", 3, "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
