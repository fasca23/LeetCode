class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Считаем частоты букв
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        length = 0
        has_odd = False
        
        for freq in count.values():
            # Берём пары: freq // 2 * 2 — это наибольшее чётное ≤ freq
            length += freq // 2 * 2
            
            # Если частота нечётная — одну букву можно в центр
            if freq % 2 == 1:
                has_odd = True
        
        # Если была нечётная буква — добавляем 1 в центр
        return length + (1 if has_odd else 0)
