"""
Length of Last Word.
LeetCode #58, Easy.

Дано: строка s со словами через пробел.
Вернуть: длину последнего слова.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Обход с конца.
        
        Пропускаем хвостовые пробелы, затем считаем буквы до пробела.
        """
        i = len(s) - 1
        length = 0
        
        # Пропускаем пробелы в конце
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Считаем буквы последнего слова
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ("Hello World", 5),
        (" fly me to the moon ", 4),
        ("luffy is still joyboy", 6),
        ("a", 1),
        (" ", 0),
        ("   day   ", 3),
    ]
    
    for s, expected in tests:
        result = sol.lengthOfLastWord(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} {s!r:30} → {result} (ожидалось {expected})")
