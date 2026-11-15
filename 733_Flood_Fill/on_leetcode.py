class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old_color = image[sr][sc]
        
        # Если цвет уже такой — ничего не делаем
        if old_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        queue = deque([(sr, sc)])
        
        while queue:
            r, c = queue.popleft()
            
            # Пропускаем если уже покрашено или другой цвет
            if image[r][c] != old_color:
                continue
            
            # Красим
            image[r][c] = color
            
            # Добавляем 4 соседей в границах
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    queue.append((nr, nc))
        
        return image
