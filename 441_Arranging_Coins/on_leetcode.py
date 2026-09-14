class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Бинарный поиск максимального k
        left, right = 1, n
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            # Сумма первых mid рядов = mid*(mid+1)/2
            total = mid * (mid + 1) // 2
            
            if total <= n:
                # Хватает монет — пробуем больше
                result = mid
                left = mid + 1
            else:
                # Не хватает — уменьшаем
                right = mid - 1
        
        return result
