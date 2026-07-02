"""
Climbing Stairs.
LeetCode #70, Easy.

Дано: число ступенек n.
Вернуть: количество способов добраться до вершины
         шагами по 1 или 2 ступеньки.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Динамическое программирование снизу вверх.
        
        Это числа Фибоначчи:
        ways(1) = 1
        ways(2) = 2
        ways(n) = ways(n-1) + ways(n-2)
        
        Оптимизация: храним только два предыдущих значения.
        """
        if n <= 2:
            return n
        
        # prev2 = ways(1), prev1 = ways(2)
        prev2, prev1 = 1, 2
        
        for i in range(3, n + 1):
            current = prev1 + prev2  # ways(i)
            prev2 = prev1            # сдвигаем окно
            prev1 = current
        
        return prev1


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (1, 1),
        (10, 89),
    ]
    
    for n, expected in tests:
        result = sol.climbStairs(n)
        status = "✓" if result == expected else "✗"
        print(f"{status} n={n:2} → {result:3} (ожидалось {expected})")
