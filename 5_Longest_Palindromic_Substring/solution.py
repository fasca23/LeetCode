"""
Longest Palindromic Substring.
LeetCode #5, Medium.

Дано: строка s.
Найти: самую длинную палиндромную подстроку.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Метод разворота от центра.
        
        Для каждой позиции пытаемся развернуть палиндром
        нечётной длины (центр — символ) и чётной (центр — между символами).
        Запоминаем самый длинный.
        """
        n = len(s)
        start, max_len = 0, 1  # хотя бы один символ — палиндром
        
        def expand(left, right):
            """Разворачиваемся от left/right, пока символы равны."""
            nonlocal start, max_len
            while left >= 0 and right < n and s[left] == s[right]:
                cur_len = right - left + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = left
                left -= 1
                right += 1
        
        for i in range(n):
            expand(i, i)      # нечётный палиндром: "aba"
            expand(i, i + 1)  # чётный палиндром:   "abba"
        
        return s[start:start + max_len]


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("aaaa", ["aaaa"]),
        ("racecar", ["racecar"]),
    ]
    
    for s, expected in tests:
        result = sol.longestPalindrome(s)
        status = "✓" if result in expected else "✗"
        print(f"{status} s={s!r:12} → {result!r} (ожидалось {expected})")