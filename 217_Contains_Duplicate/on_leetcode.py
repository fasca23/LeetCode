class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Set хранит уже встреченные числа
        seen = set()
        
        for num in nums:
            # Если число уже в set — дубликат найден
            if num in seen:
                return True
            
            # Иначе запоминаем число
            seen.add(num)
        
        # Все числа уникальны
        return False
