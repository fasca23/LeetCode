class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0  # горизонтальное смещение
        y = 0  # вертикальное смещение
        
        for ch in moves:
            if ch == 'U':
                y += 1
            elif ch == 'D':
                y -= 1
            elif ch == 'R':
                x += 1
            elif ch == 'L':
                x -= 1
        
        # Вернулся в начало если оба смещения 0
        return x == 0 and y == 0
