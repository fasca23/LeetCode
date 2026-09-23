class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        # Начинаем с √area и идём вниз
        # Первый делитель даст минимальную разницу L - W
        for w in range(int(area ** 0.5), 0, -1):
            if area % w == 0:
                # L = area // w, гарантированно L >= W
                return [area // w, w]
        
        # Сюда не дойдём — 1 всегда делитель
        return [area, 1]
