class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total = 0
        
        # Для каждой атаки кроме последней
        for i in range(len(timeSeries) - 1):
            # Разница до следующей атаки
            gap = timeSeries[i + 1] - timeSeries[i]
            # Отравление длится min(duration, gap)
            total += min(duration, gap)
        
        # Последняя атака — полный duration
        total += duration
        
        return total
