class Solution:
    def findLHS(self, nums: list[int]) -> int:
        # Считаем частоты
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        max_len = 0
        
        # Для каждого числа проверяем пару (x, x+1)
        for x in count:
            if x + 1 in count:
                # Длина = сумма частот обоих значений
                length = count[x] + count[x + 1]
                if length > max_len:
                    max_len = length
        
        return max_len
