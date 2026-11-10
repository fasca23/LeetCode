class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Ищем правее
                left = mid + 1
            else:
                # Ищем левее
                right = mid - 1
        
        # Не нашли
        return -1
