class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Словарь: значение → последний индекс где оно встретилось
        last = {}
        
        for i, num in enumerate(nums):
            # Если число уже было и расстояние ≤ k
            if num in last and i - last[num] <= k:
                return True
            
            # Обновляем последнюю позицию числа
            last[num] = i
        
        return False
