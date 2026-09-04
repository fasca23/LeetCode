class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Указатель на строку s
        i = 0
        
        # Идём по t
        for ch in t:
            # Если нашли текущий символ s — двигаем указатель
            if i < len(s) and s[i] == ch:
                i += 1
        
        # Прошли всю s — подпоследовательность
        return i == len(s)
