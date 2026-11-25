class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        
        def backtrack(i, path):
            if i == len(s):
                result.append(path)
                return
            
            ch = s[i]
            
            if ch.isdigit():
                # Цифра — один вариант
                backtrack(i + 1, path + ch)
            else:
                # Буква — два варианта
                backtrack(i + 1, path + ch.lower())
                backtrack(i + 1, path + ch.upper())
        
        backtrack(0, "")
        return result
