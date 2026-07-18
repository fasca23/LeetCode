"""Тесты для Pascal's Triangle II."""
import unittest
from solution import Solution


class TestGetRow(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, rowIndex, expected):
        result = self.sol.getRow(rowIndex)
        self.assertEqual(result, expected, f"rowIndex={rowIndex}")
    
    def test_row_0(self):
        self.check(0, [1])
    
    def test_row_1(self):
        self.check(1, [1, 1])
    
    def test_row_2(self):
        self.check(2, [1, 2, 1])
    
    def test_row_3(self):
        self.check(3, [1, 3, 3, 1])
    
    def test_row_4(self):
        self.check(4, [1, 4, 6, 4, 1])
    
    def test_row_10(self):
        self.check(10, [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
