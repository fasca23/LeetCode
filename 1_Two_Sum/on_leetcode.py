class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            need = target - num       # сколько не хватает до target
            if need in seen:          # уже встречали?
                return [seen[need], i] # нашли пару
            seen[num] = i             # запоминаем текущий