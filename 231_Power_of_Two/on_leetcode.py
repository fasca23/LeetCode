class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Степень двойки: > 0 и ровно один единичный бит
        # n & (n-1) обнуляет младший единичный бит
        # Если бит был один → результат 0
        return n > 0 and (n & (n - 1)) == 0
