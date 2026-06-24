class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, max_len = 0, 1
        
        for i in range(n):
            # нечётный
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start, max_len = l, r - l + 1
                l -= 1
                r += 1
            
            # чётный
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start, max_len = l, r - l + 1
                l -= 1
                r += 1
        
        return s[start:start + max_len]