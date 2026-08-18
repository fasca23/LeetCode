class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Начинаем с n (индекса который не попадёт в цикл)
        result = len(nums)
        
        for i, num in enumerate(nums):
            # XOR индекса и значения
            # Каждое число от 0 до n встретится дважды
            # Недостающее — только один раз
            result ^= i ^ num
        
        return result
