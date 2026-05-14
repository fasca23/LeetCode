class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        max_len = 0
        
        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            
            last[ch] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
