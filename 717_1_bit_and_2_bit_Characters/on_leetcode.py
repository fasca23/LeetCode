class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        n = len(bits)
        
        # Идём пока не дойдём до последнего элемента
        while i < n - 1:
            if bits[i] == 1:
                # 2-битный символ (10 или 11) — пропускаем 2
                i += 2
            else:
                # 1-битный символ (0) — шаг 1
                i += 1
        
        # Если остановились на последнем — он 1-битный
        return i == n - 1
