class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Алгоритм Бойера-Мура (голосование)
        # Мажоритарный элемент (> n/2) переживёт попарное исключение
        candidate = None
        count = 0
        
        for num in nums:
            # Счётчик обнулился — выбираем нового кандидата
            if count == 0:
                candidate = num
            
            # Текущий элемент = кандидат → +1 голос
            # Иначе → -1 (исключаем пару "кандидат + другой")
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        # candidate — элемент, который встречается > n/2 раз
        return candidate
