class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # Сортируем желания и размеры печенья
        g.sort()
        s.sort()
        
        i = 0  # указатель на детей
        j = 0  # указатель на печенье
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                # Печенье подходит — ребёнок доволен
                i += 1
                j += 1
            else:
                # Печенье мало — пробуем следующее
                j += 1
        
        # i = количество довольных детей
        return i
