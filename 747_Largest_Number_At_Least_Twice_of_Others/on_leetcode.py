class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_val = -1
        max_idx = -1
        second_max = -1
        
        for i, num in enumerate(nums):
            if num > max_val:
                # Новый максимум — старый становится вторым
                second_max = max_val
                max_val = num
                max_idx = i
            elif num > second_max:
                # Обновляем второй максимум
                second_max = num
        
        # Проверяем условие
        if max_val >= 2 * second_max:
            return max_idx
        return -1
