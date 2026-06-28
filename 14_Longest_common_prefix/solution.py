"""
Longest Common Prefix.
LeetCode #14, Easy.

Дано: массив строк strs.
Вернуть: самый длинный общий префикс.
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Вертикальное сканирование.
        
        Берём символы первой строки по одному.
        Проверяем что у всех строк на этой позиции тот же символ.
        """
        if not strs:
            return ""
        
        # Идём по символам первой строки
        for i, ch in enumerate(strs[0]):
            # Проверяем этот символ во всех остальных строках
            for s in strs[1:]:
                # Если строка кончилась или символ не совпал — стоп
                if i >= len(s) or s[i] != ch:
                    return strs[0][:i]
        
        # Все символы первой строки — общий префикс
        return strs[0]


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["a"], "a"),
        (["", ""], ""),
        (["ab", "a"], "a"),
    ]
    
    for strs, expected in tests:
        result = sol.longestCommonPrefix(strs)
        status = "✓" if result == expected else "✗"
        print(f"{status} {strs!s:40} → {result!r} (ожидалось {expected!r})")
