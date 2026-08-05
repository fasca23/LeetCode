class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n < 3:
            return []
        
        # Сортируем чтобы использовать два указателя
        nums.sort()
        result = []
        
        for i in range(n - 2):
            # Пропускаем дубликаты первого числа
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Ранний выход: минимальная сумма > 0
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            
            # Ранний выход: максимальная сумма < 0
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
            
            left, right = i + 1, n - 1
            target = -nums[i]  # какую сумму должны дать left + right
            
            while left < right:
                cur_sum = nums[left] + nums[right]
                
                if cur_sum == target:
                    # Нашли тройку
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Пропускаем дубликаты второго числа
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Пропускаем дубликаты третьего числа
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif cur_sum < target:
                    # Сумма маловата — двигаем левый (увеличиваем)
                    left += 1
                else:
                    # Сумма велика — двигаем правый (уменьшаем)
                    right -= 1
        
        return result
