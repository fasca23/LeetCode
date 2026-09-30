class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 1 и меньше — не совершенные
        if num <= 1:
            return False
        
        # 1 всегда делитель
        total = 1
        
        # Ищем делители до √num
        i = 2
        while i * i <= num:
            if num % i == 0:
                # i — делитель
                total += i
                # num // i — парный делитель (если не равен i)
                if i != num // i:
                    total += num // i
            i += 1
        
        return total == num
