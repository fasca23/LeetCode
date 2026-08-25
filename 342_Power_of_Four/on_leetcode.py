class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Отрицательные и 0 — не степени четвёрки
        if n <= 0:
            return False
        
        # Делим на 4 пока делится без остатка
        while n % 4 == 0:
            n //= 4
        
        # Если осталась 1 — все множители были четвёрки
        return n == 1
