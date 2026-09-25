class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Словарь: число → его следующий больший элемент
        next_greater = {}
        stack = []
        
        for num in nums2:
            # Пока стек не пуст и верхушка меньше текущего
            # Текущий num — следующий больший для верхушки
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            
            stack.append(num)
        
        # Для чисел из nums1 берём из словаря или -1
        return [next_greater.get(x, -1) for x in nums1]
