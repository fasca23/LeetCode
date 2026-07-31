class Solution:
    def hammingWeight(self, n: int) -> int:
        # Считаем количество единичных битов
        count = 0
        
        while n != 0:
            # n & (n-1) обнуляет младший единичный бит
            # Пример: 10100 & 10011 = 10000 (младшая 1 исчезла)
            n = n & (n - 1)
            count += 1
        
        return count
