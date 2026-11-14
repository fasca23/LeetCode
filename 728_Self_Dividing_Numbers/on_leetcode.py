class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []
        
        for num in range(left, right + 1):
            # Проверяем каждую цифру
            is_valid = True
            for digit_ch in str(num):
                digit = int(digit_ch)
                # 0 — нельзя делить, или не делится без остатка
                if digit == 0 or num % digit != 0:
                    is_valid = False
                    break
            
            if is_valid:
                result.append(num)
        
        return result
