"""
Longest Substring Without Repeating Characters.
LeetCode #3, Medium.

Поиск длины самой длинной подстроки без повторяющихся символов.
Метод: скользящее окно со словарём позиций. O(n).
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Возвращает длину самой длинной подстроки без повторов.
        
        Идея: словарь last хранит индекс последнего появления символа.
        Левая граница окна left сдвигается сразу за дубликат.
        """
        last = {}          # символ → последний индекс
        left = 0           # левая граница окна
        max_len = 0        # максимальная длина
        
        for right, ch in enumerate(s):
            # Если символ уже был в окне — перепрыгиваем left
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            
            # Обновляем позицию символа
            last[ch] = right
            
            # Длина текущего окна
            current = right - left + 1
            if current > max_len:
                max_len = current
        
        return max_len


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
    ]
    
    for s, expected in tests:
        result = sol.lengthOfLongestSubstring(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} s={s!r:15} → {result} (ожидалось {expected})")
