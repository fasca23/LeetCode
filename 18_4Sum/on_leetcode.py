class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        if n < 4:
            return []
        
        nums.sort()
        result = []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
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
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif cur_sum < need:
                        left += 1
                    else:
                        right -= 1
        
        return result
