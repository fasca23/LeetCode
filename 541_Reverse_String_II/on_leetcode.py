class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)
        
        # Шагаем блоками по 2k
        for i in range(0, n, 2 * k):
            # Разворачиваем первые k символов блока
            left = i
            # Если символов меньше k — берём до конца
            right = min(i + k - 1, n - 1)
            
            # Разворот на месте
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        return "".join(chars)
