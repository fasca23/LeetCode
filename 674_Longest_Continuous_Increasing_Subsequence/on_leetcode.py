class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        count = 1       # текущая серия
        max_count = 1   # максимальная серия
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # Серия продолжается
                count += 1
                if count > max_count:
                    max_count = count
            else:
                # Серия прервалась
                count = 1
        
        return max_count
