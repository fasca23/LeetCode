class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Считаем частоты букв в magazine
        count = {}
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1
        
        # Проверяем хватает ли букв для ransomNote
        for ch in ransomNote:
            # Буквы нет или уже исчерпана
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1
        
        return True
