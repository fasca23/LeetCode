"""Тесты для Add Two Numbers."""
import unittest
from solution import Solution, to_linked, to_list


class TestAddTwoNumbers(unittest.TestCase):
    
    def check(self, a, b, expected):
        """Проверить: a + b = expected."""
        l1 = to_linked(a)
        l2 = to_linked(b)
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(to_list(result), expected)
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check([2, 4, 3], [5, 6, 4], [7, 0, 8])   # 342 + 465 = 807
    
    def test_example_2(self):
        self.check([0], [0], [0])                       # 0 + 0 = 0
    
    def test_example_3(self):
        self.check([9]*7, [9]*4, [8,9,9,9,0,0,0,1])    # 9999999 + 9999
    
    # ---------- Разная длина ----------
    def test_different_length(self):
        self.check([0, 0, 1], [1], [1, 0, 1])           # 100 + 1 = 101
        self.check([1], [0, 0, 1], [1, 0, 1])           # 1 + 100 = 101
    
    # ---------- Перенос ----------
    def test_carry(self):
        self.check([9, 9, 9], [1], [0, 0, 0, 1])        # 999 + 1 = 1000
        self.check([5, 5, 5], [5, 5, 5], [0, 1, 1, 1])  # 555 + 555 = 1110
        self.check([5], [5], [0, 1])                     # 5 + 5 = 10
    
    # ---------- Граничные ----------
    def test_zero(self):
        self.check([0], [1, 2, 3], [1, 2, 3])           # 0 + 321 = 321
        self.check([4, 5, 6], [0], [4, 5, 6])           # 654 + 0 = 654
    
    # ---------- Чистота ----------
    def test_input_not_modified(self):
        l1 = to_linked([2, 4, 3])
        l2 = to_linked([5, 6, 4])
        before = to_list(l1), to_list(l2)
        Solution().addTwoNumbers(l1, l2)
        self.assertEqual((to_list(l1), to_list(l2)), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)