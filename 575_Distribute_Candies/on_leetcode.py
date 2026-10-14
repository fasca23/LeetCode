class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        # Количество уникальных типов
        unique = len(set(candyType))
        
        # Сестра получит половину всех конфет
        half = len(candyType) // 2
        
        # Максимум = минимум из двух
        return min(unique, half)
