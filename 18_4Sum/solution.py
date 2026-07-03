"""
4Sum.
LeetCode #18, Medium.

Дано: массив nums, цель target.
Вернуть: все уникальные четвёрки чисел с суммой равной target.
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Сортировка + два указателя.
        
        Фиксируем i, j (первые два числа).
        Для оставшейся части — два указателя left/right
        ищут пару с суммой target - nums[i] - nums[j].
        Пропускаем дубликаты на всех уровнях.
        """
        n = len(nums)
        if n < 4:
            return []
        
        nums.sort()
        result = []
        
        for i in range(n - 3):
            # Пропускаем дубликаты для первого числа
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Ранний выход: минимальная сумма > target
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            
            # Ранний выход: максимальная сумма < target
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            
            for j in range(i + 1, n - 2):
                # Пропускаем дубликаты для второго числа
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Ранний выход для j
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                
                left, right = j + 1, n - 1
                need = target - nums[i] - nums[j]
                
                while left < right:
                    cur_sum = nums[left] + nums[right]
                    
                    if cur_sum == need:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        # Пропускаем дубликаты третьего числа
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # Пропускаем дубликаты четвёртого числа
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    
                    elif cur_sum < need:
                        left += 1
                    else:
                        right -= 1
        
        return result


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([0, 0, 0, 0], 0, [[0, 0, 0, 0]]),
        ([1, -2, -5, -4, -3, 3, 3, 5], -11, [[-5, -4, -3, 1]]),
    ]
    
    for nums, target, expected in tests:
        result = sol.fourSum(nums, target)
        # Сортируем для сравнения
        result_sorted = sorted([sorted(q) for q in result])
        expected_sorted = sorted([sorted(q) for q in expected])
        status = "✓" if result_sorted == expected_sorted else "✗"
        print(f"{status} nums={nums}, target={target}")
        print(f"   → {result}")
