class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        
        for ch in s:
            # Если заглавная буква (A-Z)
            if 'A' <= ch <= 'Z':
                # Заменяем на строчную: сдвиг +32 в ASCII
                # ord('A')=65, ord('a')=97, разница = 32
                result.append(chr(ord(ch) + 32))
            else:
                result.append(ch)
        
        return ''.join(result)
