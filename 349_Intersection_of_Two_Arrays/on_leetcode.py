class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Множество из первого массива — убирает дубликаты
        set1 = set(nums1)
        
        # Результат тоже множество — уникальные элементы
        result = set()
        
        # Проверяем каждый элемент второго массива
        for num in nums2:
            if num in set1:
                result.add(num)
        
        return list(result)
