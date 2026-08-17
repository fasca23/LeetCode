class Solution:
    def isUgly(self, n: int) -> bool:
        # Отрицательные и 0 — не уродливые
        if n <= 0:
            return False
        
        # Делим на 2, 3, 5 пока возможно
        for divisor in [2, 3, 5]:
            while n % divisor == 0:
                n //= divisor
        
        # Если осталась 1 — все множители были 2/3/5
        return n == 1
