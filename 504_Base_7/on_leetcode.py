class Solution:
    def convertToBase7(self, num: int) -> str:
        # 0 — особый случай
        if num == 0:
            return "0"
        
        # Знак
        sign = "-" if num < 0 else ""
        num = abs(num)
        
        result = ""
        while num > 0:
            # Остаток от деления на 7 — текущая цифра
            result = str(num % 7) + result
            num //= 7
        
        return sign + result
