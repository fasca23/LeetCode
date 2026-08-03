class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Два указателя: слева и справа
        left = 0
        right = len(height) - 1
        max_area = 0
        
        # Сходимся к центру
        while left < right:
            # Высота контейнера = меньшая из двух линий
            # Ширина = расстояние между указателями
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            
            # Обновляем максимум
            if area > max_area:
                max_area = area
            
            # Двигаем меньшую высоту
            # Если равны — без разницы какую, двигаем левую
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
