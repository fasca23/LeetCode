class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0       # текущая серия единиц
        max_count = 0   # максимальная серия
        
        for num in nums:
            if num == 1:
                count += 1
                # Обновляем максимум
                if count > max_count:
                    max_count = count
            else:
                # Серия прервалась — сбрасываем
                count = 0
        
        return max_count
