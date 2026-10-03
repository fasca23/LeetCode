class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # Строки одинаковые — необычной подпоследовательности нет
        if a == b:
            return -1
        
        # Строки разные — самая длинная из них и есть ответ
        return max(len(a), len(b))
