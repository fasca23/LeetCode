class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Минимальная цена, которую мы видели до текущего дня
        # Изначально — бесконечность, чтобы любая цена была меньше
        min_price = float('inf')
        
        # Максимальная прибыль, которую можно получить
        max_profit = 0
        
        for price in prices:
            # Если текущая цена ниже минимума — обновляем минимум
            # (это лучший день для покупки)
            if price < min_price:
                min_price = price
            
            # Считаем прибыль если продать сегодня
            profit = price - min_price
            
            # Если прибыль больше максимальной — обновляем
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
