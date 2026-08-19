class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # Позиция для следующего ненулевого элемента
        pos = 0
        
        # Переносим все ненулевые в начало
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        
        # Заполняем оставшийся хвост нулями
        for j in range(pos, len(nums)):
            nums[j] = 0
