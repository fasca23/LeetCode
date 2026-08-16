class Solution:
    def addDigits(self, num: int) -> int:
        # Числовой корень через остаток от деления на 9
        # 0 → 0
        if num == 0:
            return 0
        
        # Кратно 9 → 9 (например: 18 → 1+8 = 9)
        if num % 9 == 0:
            return 9
        
        # Иначе — остаток от деления на 9
        # 38 → 3+8=11 → 1+1=2, и 38 % 9 = 2
        return num % 9
