class Solution:
    def fib(self, n: int) -> int:
        # База: F(0) = 0, F(1) = 1
        if n <= 1:
            return n
        
        # Два предыдущих значения
        prev2, prev1 = 0, 1
        
        for i in range(2, n + 1):
            # Текущее = сумма двух предыдущих
            cur = prev1 + prev2
            # Сдвигаем окно
            prev2 = prev1
            prev1 = cur
        
        return prev1
