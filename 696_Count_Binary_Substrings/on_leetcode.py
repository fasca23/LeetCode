class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        count = 1
        
        # Группируем подряд идущие одинаковые символы
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)
        
        # Для каждой пары соседних групп: min(len1, len2) валидных подстрок
        total = 0
        for i in range(1, len(groups)):
            total += min(groups[i - 1], groups[i])
        
        return total
