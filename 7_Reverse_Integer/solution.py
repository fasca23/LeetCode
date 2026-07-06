"""
Reverse Integer.
LeetCode #7, Medium.

Дано: 32-битное целое число x.
Вернуть: цифры в обратном порядке.
Если переполнение — 0.
"""


class Solution:
    def reverse(self, x: int) -> int:
        """
        Отщипываем цифры с конца.
        
        На каждом шаге:
        digit = x % 10   — последняя цифра
        rev = rev * 10 + digit
        x //= 10
        
        Проверяем переполнение ДО умножения rev * 10.
        """
        # Границы 32-битного int
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Определяем знак, работаем с абсолютным значением
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Проверяем переполнение ДО операции
            # rev * 10 + digit > INT_MAX ?
            if rev > (INT_MAX - digit) // 10:
                return 0
            
            rev = rev * 10 + digit
        
        return sign * rev


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),  # переполнение
    ]
    
    for x, expected in tests:
        result = sol.reverse(x)
        status = "✓" if result == expected else "✗"
        print(f"{status} x={x:12} → {result} (ожидалось {expected})")
