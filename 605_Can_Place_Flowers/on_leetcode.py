class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            # Проверяем левого соседа (или край)
            left_ok = (i == 0 or flowerbed[i - 1] == 0)
            # Проверяем правого соседа (или край)
            right_ok = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            
            # Текущая клетка пуста и соседи не мешают
            if flowerbed[i] == 0 and left_ok and right_ok:
                flowerbed[i] = 1  # сажаем
                n -= 1
                if n == 0:
                    return True
        
        return n <= 0
