"""Тесты для Longest Common Prefix."""
import unittest
from solution import Solution


class TestLongestCommonPrefix(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def check(self, strs, expected):
        result = self.sol.longestCommonPrefix(strs)
        self.assertEqual(result, expected, f"strs={strs}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check(["flower", "flow", "flight"], "fl")
    
    def test_example_2(self):
        self.check(["dog", "racecar", "car"], "")
    
    # ---------- Граничные ----------
    def test_empty_array(self):
        self.check([], "")
    
    def test_one_string(self):
        self.check(["a"], "a")
    
    def test_all_same(self):
        self.check(["abc", "abc", "abc"], "abc")
    
    def test_no_prefix(self):
        self.check(["abc", "def", "ghi"], "")
    
    def test_empty_strings(self):
        self.check(["", ""], "")
    
    def test_mixed_length(self):
        self.check(["ab", "a"], "a")


if __name__ == "__main__":
    unittest.main(verbosity=2)
