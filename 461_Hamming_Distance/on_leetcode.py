class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR даёт 1 на позициях где биты разные
        xor = x ^ y
        
        count = 0
        while xor:
            # Обнуляем младший единичный бит
            xor &= xor - 1
            count += 1
        
        return count
