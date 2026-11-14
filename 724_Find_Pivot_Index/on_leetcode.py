class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # Правая сумма = total - left_sum - num (текущий)
            right_sum = total - left_sum - num
            
            if left_sum == right_sum:
                return i
            
            # Накапливаем левую сумму
            left_sum += num
        
        # Pivot не найден
        return -1
