"""
Regular Expression Matching.
LeetCode #10, Hard.

Дано: строка s и шаблон p с . и *.
Вернуть: true если s полностью совпадает с шаблоном.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Динамическое программирование.
        
        dp[i][j] — совпадают ли s[:i] и p[:j].
        
        Правила:
        - если p[j-1] == '.' или s[i-1] == p[j-1] → текущий символ совпал
        - если p[j-1] == '*' → либо ноль повторений (пропускаем шаблон),
          либо одно+ повторений (если предыдущий символ совпал)
        """
        m, n = len(s), len(p)
        
        # dp[i][j]: s[:i] совпадает с p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Пустая строка и пустой шаблон
        dp[0][0] = True
        
        # Пустая строка против шаблона с *
        # a*, a*b*, a*b*c* — могут дать пустую строку
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Два варианта:
                    # 1. Ноль повторений — пропускаем "x*"
                    dp[i][j] = dp[i][j - 2]
                    
                    # 2. Одно+ повторений — если символ перед * совпадает с s[i-1]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                
                else:
                    # Обычный символ или .
                    if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("", ".*", True),
        ("", "", True),
    ]
    
    for s, p, expected in tests:
        result = sol.isMatch(s, p)
        status = "✓" if result == expected else "✗"
        print(f"{status} s={s!r:15} p={p!r:15} → {result} (ожидалось {expected})")
