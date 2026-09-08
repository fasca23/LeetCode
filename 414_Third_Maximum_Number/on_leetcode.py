class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # Убираем дубликаты и сортируем по убыванию
        unique = sorted(set(nums), reverse=True)
        
        # Если уникальных меньше 3 — возвращаем максимум
        if len(unique) < 3:
            return unique[0]
        
        # Третье по величине
        return unique[2]
