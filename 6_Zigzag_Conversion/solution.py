"""
Zigzag Conversion.
LeetCode #6, Medium.

Дано: строка s, число строк numRows.
Вернуть: строку после зигзаг-преобразования.
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Симуляция движения по строкам.
        
        Идём по строке, раскладываем символы в список строк.
        Направление меняется при достижении верхней/нижней границы.
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Список строк для каждого ряда
        rows = [''] * numRows
        row = 0          # текущая строка
        step = 1         # направление: 1 = вниз, -1 = вверх
        
        for ch in s:
            rows[row] += ch
            
            # Меняем направление на границах
            if row == 0:
                step = 1        # идём вниз
            elif row == numRows - 1:
                step = -1       # идём вверх
            
            row += step
        
        return ''.join(rows)


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("AB", 1, "AB"),
        ("ABCD", 2, "ACBD"),
    ]
    
    for s, numRows, expected in tests:
        result = sol.convert(s, numRows)
        status = "✓" if result == expected else "✗"
        print(f"{status} s={s!r:20} rows={numRows} → {result!r} (ожидалось {expected!r})")
