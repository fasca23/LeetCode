class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Отрицательные и 0 — не степени тройки
        if n <= 0:
            return False
        
        # Делим на 3 пока делится без остатка
        while n % 3 == 0:
            n //= 3
        
        # Если осталась 1 — все множители были тройки
        return n == 1
