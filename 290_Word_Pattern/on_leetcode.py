class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # Количество букв и слов должно совпадать
        if len(pattern) != len(words):
            return False
        
        # Два словаря: буква→слово и слово→буква
        map_ps = {}  # pattern → s
        map_sp = {}  # s → pattern
        
        for ch, word in zip(pattern, words):
            # Буква уже связана с другим словом
            if ch in map_ps and map_ps[ch] != word:
                return False
            
            # Слово уже связано с другой буквой
            if word in map_sp and map_sp[word] != ch:
                return False
            
            # Сохраняем связи
            map_ps[ch] = word
            map_sp[word] = ch
        
        return True
