class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # Ищем первый индекс где отличается
        left = 0
        while left < n and nums[left] == sorted_nums[left]:
            left += 1
        
        # Ищем последний индекс где отличается
        right = n - 1
        while right >= 0 and nums[right] == sorted_nums[right]:
            right -= 1
        
        # Если left > right — массив уже отсортирован
        if left > right:
            return 0
        
        return right - left + 1
