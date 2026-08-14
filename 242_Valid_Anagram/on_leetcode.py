class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Разная длина — точно не анаграмма
        if len(s) != len(t):
            return False
        
        # Считаем частоты символов
        count = {}
        
        # Добавляем частоты из s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        # Вычитаем частоты из t
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            # Если ушли в минус — в t больше этого символа чем в s
            if count[ch] < 0:
                return False
        
        return True
