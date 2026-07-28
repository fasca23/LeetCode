class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        
        for ch in columnTitle:
            # Превращаем букву в число: A→1, B→2, ..., Z→26
            # ord(ch) — ASCII-код буквы
            # ord('A') = 65, ord('B') = 66, ...
            # A: 65 - 65 + 1 = 1
            # Z: 90 - 65 + 1 = 26
            value = ord(ch) - ord('A') + 1
            
            # Сдвигаем накопленный результат на 1 разряд влево
            # и добавляем текущую цифру
            # "AB": A=1 → 1, B=2 → 1*26+2=28
            result = result * 26 + value
        
        return result
