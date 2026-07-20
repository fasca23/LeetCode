class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Храним все ряды треугольника
        # Первый ряд всегда [1]
        triangle = [[1]]
        
        # Строим ряды от 1 до numRows-1 (нумерация с 0)
        for i in range(1, numRows):
            # Берём предыдущий ряд для расчётов
            prev_row = triangle[-1]
            
            # Новый ряд: левый край всегда 1
            row = [1]
            
            # Заполняем середину: каждый элемент = сумма двух верхних
            # prev_row[j-1] — верхний левый
            # prev_row[j]   — верхний правый
            for j in range(1, len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])
            
            # Правый край всегда 1
            row.append(1)
            
            # Добавляем ряд в треугольник
            triangle.append(row)
        
        return triangle
