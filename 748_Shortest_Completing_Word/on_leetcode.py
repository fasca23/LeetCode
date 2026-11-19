from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        # Нужные буквы и их количество (только буквы, lowercase)
        need = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        
        result = None
        
        for word in words:
            have = Counter(word)
            # Проверяем: все нужные буквы есть в достаточном количестве
            if all(have[c] >= need[c] for c in need):
                # Кандидат — берём кратчайшее
                if result is None or len(word) < len(result):
                    result = word
        
        return result
