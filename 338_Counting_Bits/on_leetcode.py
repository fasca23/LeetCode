class Solution:
    def countBits(self, n: int) -> list[int]:
        # Массив результата: ans[i] = количество единиц в числе i
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # i >> 1 — это i // 2 (сдвиг вправо)
            # i & 1  — младший бит (0 или 1)
            # Количество единиц в i = количество в i//2 + последний бит
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans
