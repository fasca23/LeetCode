"""
Roman to Integer.
LeetCode #13, Easy.

Дано: строка s с римским числом.
Вернуть: целое число.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Обход справа налево.
        
        Если текущее значение меньше предыдущего — вычитаем (IV=4).
        Иначе — складываем.
        """
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev = 0  # значение предыдущего (более правого) символа
        
        # Идём справа налево
        for ch in reversed(s):
            cur = values[ch]
            if cur < prev:
                total -= cur  # IV → 5-1=4
            else:
                total += cur  # VI → 5+1=6
            prev = cur
        
        return total


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
    ]
    
    for s, expected in tests:
        result = sol.romanToInt(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} {s:10} → {result:5} (ожидалось {expected})")