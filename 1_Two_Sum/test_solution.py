"""Тесты для Two Sum."""
import unittest
from solution import Solution


class TestTwoSum(unittest.TestCase):
    
    def check(self, nums, target, expected):
        result = Solution().twoSum(nums, target)
        i, j = result
        self.assertEqual(nums[i] + nums[j], target,
                         f"Сумма не совпадает: {nums[i]}+{nums[j]} ≠ {target}")
        self.assertNotEqual(i, j, "Индексы должны быть разными")
        # Порядок не важен
        self.assertEqual(set(result), set(expected),
                         f"Индексы: {result}, ожидалось: {expected}")
    
    # ---------- Из условия ----------
    def test_example_1(self):
        self.check([2, 7, 11, 15], 9, [0, 1])
    
    def test_example_2(self):
        self.check([3, 2, 4], 6, [1, 2])
    
    def test_example_3(self):
        self.check([3, 3], 6, [0, 1])
    
    # ---------- Разное ----------
    def test_negative(self):
        self.check([-1, -2, -3, -4], -6, [1, 3])
    
    def test_with_zero(self):
        self.check([0, 4, 3, 0], 0, [0, 3])
    
    def test_large(self):
        self.check([1, 10, 100, 1000], 1100, [2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)