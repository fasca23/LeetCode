"""
Pascal's Triangle II.
LeetCode #119, Easy.

Дано: число rowIndex.
Вернуть: rowIndex-ю строку треугольника Паскаля.
"""


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        """
        Одна строка, обновление справа налево.
        
        Начинаем с [1]. Для каждого нового ряда:
        добавляем 1 в конец, затем обновляем элементы
        справа налево: row[j] = row[j] + row[j-1].
        """
        row = [1]
        
        for i in range(1, rowIndex + 1):
            # Добавляем правую единицу
            row.append(1)
            
            # Обновляем середину справа налево
            # Справа налево — чтобы не затереть row[j-1]
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        
        return row


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
        (4, [1, 4, 6, 4, 1]),
    ]
    
    for rowIndex, expected in tests:
        result = sol.getRow(rowIndex)
        status = "✓" if result == expected else "✗"
        print(f"{status} rowIndex={rowIndex} → {result} (ожидалось {expected})")
