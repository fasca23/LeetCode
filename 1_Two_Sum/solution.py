"""
Two Sum.
LeetCode #1, Easy.

Дано: массив nums, число target.
Найти: индексы двух элементов с суммой target.
"""


class Solution:
    def twoSum(self, nums, target):
        """
        Поиск двух индексов за O(n) через словарь.
        
        Идём по массиву. Для каждого элемента вычисляем,
        сколько не хватает до target. Если это число уже
        встречалось — возвращаем его индекс и текущий.
        """
        seen = {}  # значение → индекс
        
        for i, num in enumerate(nums):
            need = target - num          # сколько не хватает
            if need in seen:             # уже встречали?
                return [seen[need], i]   # нашли пару
            seen[num] = i                # запоминаем текущий
        
        return []  # по условию задачи не достижимо


# ------------------------ Помощники ------------------------

def check(nums, target):
    """Проверить и напечатать результат."""
    result = Solution().twoSum(nums, target)
    i, j = result
    total = nums[i] + nums[j]
    status = "✓" if total == target else "✗"
    print(f"{status} nums={nums}, target={target} → {result} "
          f"(nums[{i}]={nums[i]} + nums[{j}]={nums[j]} = {total})")


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    check([2, 7, 11, 15], 9)
    check([3, 2, 4], 6)
    check([3, 3], 6)
    check([1, 5, 9, 3], 8)