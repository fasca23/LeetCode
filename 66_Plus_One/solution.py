"""
Plus One.
LeetCode #66, Easy.

Дано: массив цифр digits.
Вернуть: массив цифр после прибавления единицы.
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Обход с конца с переносом.
        
        Идём справа налево. Если цифра < 9 — увеличиваем и выходим.
        Если 9 — превращаем в 0 и переносим 1 дальше.
        Если дошли до начала — добавляем 1 в начало (все были 9).
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # Все цифры были 9 → [9,9,9] становится [1,0,0,0]
        return [1] + digits


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([0], [1]),
    ]
    
    for digits, expected in tests:
        result = sol.plusOne(digits[:])  # копия чтобы не портить исходник
        status = "✓" if result == expected else "✗"
        print(f"{status} {digits!s:15} → {result} (ожидалось {expected})")
