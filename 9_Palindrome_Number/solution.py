"""
Palindrome Number.
LeetCode #9, Easy.

Дано: целое число x.
Определить: палиндром ли (без перевода в строку).
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Переворот половины числа.
        
        Отрицательные и кратные 10 (кроме 0) — не палиндромы.
        Переворачиваем правую половину, пока она меньше левой.
        Сравниваем: для чётной длины x == rev,
        для нечётной x == rev // 10 (средняя цифра не важна).
        """
        # Отрицательные и оканчивающиеся на 0 (кроме 0) — не палиндромы
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev = 0
        while x > rev:
            # Отщипляем последнюю цифру от x и добавляем к rev
            rev = rev * 10 + x % 10
            x //= 10
        
        # x == rev        — чётное количество цифр: 1221 → 12 == 12
        # x == rev // 10  — нечётное количество цифр: 121 → 1 == 12 // 10
        return x == rev or x == rev // 10


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (1221, True),
        (12321, True),
    ]
    
    for x, expected in tests:
        result = sol.isPalindrome(x)
        status = "✓" if result == expected else "✗"
        print(f"{status} x={x:6} → {result} (ожидалось {expected})")