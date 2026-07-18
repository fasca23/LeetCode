class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Начинаем с первого ряда: [1]
        row = [1]
        
        # Строим ряды от 1 до rowIndex
        for i in range(1, rowIndex + 1):
            # Правый край — всегда 1, добавляем в конец
            row.append(1)
            
            # Обновляем середину справа налево
            # j идёт от i-1 до 1 (края не трогаем)
            # row[j] = row[j] + row[j-1] — сумма двух верхних
            # Справа налево чтобы row[j-1] был ещё от ПРЕДЫДУЩЕГО ряда
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        
        return row
