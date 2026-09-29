class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        # Сортируем (индекс, очки) по убыванию очков
        pairs = sorted(enumerate(score), key=lambda x: -x[1])
        
        result = [""] * len(score)
        
        for rank, (idx, val) in enumerate(pairs):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)
        
        return result
