class Solution:
    def reverseVowels(self, s: str) -> str:
        # Множество гласных (верхний и нижний регистр)
        vowels = set("aeiouAEIOU")
        
        # Строку в список для изменения на месте
        chars = list(s)
        left, right = 0, len(chars) - 1
        
        while left < right:
            # Ищем гласную слева
            if chars[left] not in vowels:
                left += 1
                continue
            
            # Ищем гласную справа
            if chars[right] not in vowels:
                right -= 1
                continue
            
            # Обе гласные — меняем местами
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        
        return "".join(chars)
