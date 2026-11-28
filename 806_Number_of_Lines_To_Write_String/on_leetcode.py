class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        lines = 1
        current_width = 0
        
        for ch in s:
            # Ширина текущей буквы
            w = widths[ord(ch) - ord('a')]
            
            if current_width + w > 100:
                # Не влезает — новая строка
                lines += 1
                current_width = w
            else:
                # Влезает — добавляем
                current_width += w
        
        return [lines, current_width]
