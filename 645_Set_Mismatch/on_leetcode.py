class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        count = [0] * (n + 1)
        
        # Считаем частоты
        for num in nums:
            count[num] += 1
        
        duplicate = missing = 0
        
        # Ищем дубликат (частота 2) и отсутствующее (частота 0)
        for i in range(1, n + 1):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing = i
        
        return [duplicate, missing]
