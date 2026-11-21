class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        # Сравниваем каждый элемент с верхним-левым
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        
        return True
