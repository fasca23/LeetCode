class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        
        # XOR всех символов s
        for ch in s:
            result ^= ord(ch)
        
        # XOR всех символов t
        for ch in t:
            result ^= ord(ch)
        
        # Остался только добавленный символ
        return chr(result)
