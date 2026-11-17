class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        
        # База: стоимость на первой и второй ступеньке
        prev2 = cost[0]
        prev1 = cost[1]
        
        for i in range(2, n):
            # Текущая = cost[i] + минимум из двух предыдущих
            cur = cost[i] + min(prev2, prev1)
            # Сдвигаем окно
            prev2 = prev1
            prev1 = cur
        
        # Можно закончить на n-1 или n-2 (шаг за вершину)
        return min(prev2, prev1)
