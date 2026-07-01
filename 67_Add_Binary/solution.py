"""
Add Binary.
LeetCode #67, Easy.

Дано: две бинарные строки a и b.
Вернуть: сумму в виде бинарной строки.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Поразрядное сложение с конца.
        
        Идём справа налево, складываем биты + carry.
        Сумма: 0, 1, 2 или 3.
        Текущий бит = сумма % 2, перенос = сумма // 2.
        """
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Идём пока есть биты или перенос
        while i >= 0 or j >= 0 or carry:
            # Берём бит или 0, если строка кончилась
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            total = bit_a + bit_b + carry
            result.append(str(total % 2))  # текущий бит
            carry = total // 2              # перенос
            
            i -= 1
            j -= 1
        
        # Результат собрали задом наперёд — переворачиваем
        return ''.join(reversed(result))


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("0", "0", "0"),
        ("1", "0", "1"),
        ("111", "111", "1110"),
    ]
    
    for a, b, expected in tests:
        result = sol.addBinary(a, b)
        status = "✓" if result == expected else "✗"
        print(f"{status} {a!r} + {b!r} = {result!r} (ожидалось {expected!r})")
