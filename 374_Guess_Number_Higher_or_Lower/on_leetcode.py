class Solution:
    def guessNumber(self, n: int) -> int:
        # Бинарный поиск в диапазоне [1, n]
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            
            if result == 0:
                # Угадали
                return mid
            elif result == -1:
                # Загаданное меньше — ищем левее
                right = mid - 1
            else:
                # Загаданное больше — ищем правее
                left = mid + 1
        
        # По условию ответ всегда есть, сюда не дойдём
        return -1
