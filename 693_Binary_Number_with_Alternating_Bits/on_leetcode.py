class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # XOR со сдвигом: если биты чередуются — все единицы
        x = n ^ (n >> 1)
        
        # Проверка что x = 111...111
        # Для числа из всех единиц: x & (x+1) == 0
        return (x & (x + 1)) == 0
