"""
3Sum Closest.
LeetCode #16, Medium.

Дано: массив nums, цель target.
Вернуть: сумму трёх чисел, ближайшую к target.
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """
        Сортировка + два указателя.
        
        Фиксируем первое число (i). Для оставшейся части
        двумя указателями ищем пару с суммой ближайшей к target - nums[i].
        Запоминаем минимальную разницу.
        """
        n = len(nums)
        nums.sort()
        
        # Инициализируем большим числом
        closest = float('inf')
        
        for i in range(n - 2):
            # Пропускаем дубликаты первого числа
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                
                # Если нашли точно target — это лучший результат
                if cur_sum == target:
                    return target
                
                # Обновляем ближайшую сумму
                if abs(cur_sum - target) < abs(closest - target):
                    closest = cur_sum
                
                # Двигаем указатели
                if cur_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([1, 1, 1, 0], -100, 2),
        ([4, 0, 5, -5, 3, 3], -1, -1),
    ]
    
    for nums, target, expected in tests:
        result = sol.threeSumClosest(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums}, target={target} → {result} (ожидалось {expected})")
