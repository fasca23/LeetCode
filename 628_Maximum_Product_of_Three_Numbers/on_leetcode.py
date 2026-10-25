class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        
        # Три наибольших
        case1 = nums[-1] * nums[-2] * nums[-3]
        
        # Два наименьших (могут быть отрицательными) и наибольший
        case2 = nums[0] * nums[1] * nums[-1]
        
        return max(case1, case2)
