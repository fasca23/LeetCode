class Solution:
    def isHappy(self, n: int) -> bool:
        # Храним уже встреченные числа
        # Если число повторилось — мы в цикле → не счастливое
        seen = set()
        
        while n != 1:
            # Зациклились — число уже встречалось
            if n in seen:
                return False
            
            seen.add(n)
            
            # Считаем сумму квадратов цифр
            # Например: 19 → 1² + 9² = 1 + 81 = 82
            total = 0
            while n > 0:
                digit = n % 10           # последняя цифра
                total += digit * digit   # квадрат цифры
                n //= 10                 # убираем последнюю цифру
            
            n = total
        
        # Дошли до 1 — счастливое
        return True
