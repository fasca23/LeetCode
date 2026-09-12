class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        # Идём пока есть цифры или перенос
        while i >= 0 or j >= 0 or carry:
            # Берём цифру или 0, если строка кончилась
            d1 = int(num1[i]) if i >= 0 else 0
            d2 = int(num2[j]) if j >= 0 else 0
            
            total = d1 + d2 + carry
            result.append(str(total % 10))  # текущая цифра
            carry = total // 10              # перенос
            
            i -= 1
            j -= 1
        
        # Результат собран задом наперёд — разворачиваем
        return "".join(reversed(result))
