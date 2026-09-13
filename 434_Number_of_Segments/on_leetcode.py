class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        
        for i, ch in enumerate(s):
            # Текущий символ не пробел И
            # (это начало строки ИЛИ предыдущий был пробел)
            if ch != ' ' and (i == 0 or s[i - 1] == ' '):
                count += 1
        
        return count
