class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Первый проход: помечаем встречаемые числа
        for num in nums:
            # Индекс который соответствует числу num
            idx = abs(num) - 1
            # Помечаем отрицательным (если ещё не помечен)
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        # Второй проход: положительные значения = пропавшие числа
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                # Число i+1 отсутствует
                result.append(i + 1)
        
        return result
