class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        count = {}  # частота
        first = {}  # первый индекс
        last = {}   # последний индекс
        
        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            if num not in first:
                first[num] = i
            last[num] = i
        
        # Степень массива
        degree = max(count.values())
        
        # Минимальная длина подмассива со степенью degree
        min_len = float('inf')
        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                if length < min_len:
                    min_len = length
        
        return min_len
