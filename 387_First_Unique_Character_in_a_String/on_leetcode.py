class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Первый проход: считаем частоты всех символов
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        # Второй проход: ищем первый символ с частотой 1
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        
        # Уникальных нет
        return -1
