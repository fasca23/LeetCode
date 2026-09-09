class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        
        closest = float('inf')
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                
                if cur_sum == target:
                    return target
                
                if abs(cur_sum - target) < abs(closest - target):
                    closest = cur_sum
                
                if cur_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest