class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        
        result = []
        start = nums[0]  # начало текущего диапазона
        
        for i in range(1, len(nums)):
            # Если разрыв между текущим и предыдущим > 1
            if nums[i] != nums[i - 1] + 1:
                # Закрываем диапазон
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                
                # Начинаем новый
                start = nums[i]
        
        # Закрываем последний диапазон
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result
