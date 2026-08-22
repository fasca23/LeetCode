class NumArray:
    def __init__(self, nums: list[int]):
        # Префиксные суммы: prefix[i] = сумма nums[0..i-1]
        # prefix[0] = 0 (пустой префикс)
        self.prefix = [0]
        
        for num in nums:
            # Добавляем текущую сумму
            self.prefix.append(self.prefix[-1] + num)
    
    def sumRange(self, left: int, right: int) -> int:
        # Сумма от left до right = сумма до right включительно
        # минус сумма до left (не включая left)
        return self.prefix[right + 1] - self.prefix[left]
