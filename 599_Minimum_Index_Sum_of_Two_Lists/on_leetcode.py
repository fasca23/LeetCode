class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        # Словарь: ресторан → индекс в list1
        index1 = {}
        for i, name in enumerate(list1):
            index1[name] = i
        
        min_sum = float('inf')
        result = []
        
        for j, name in enumerate(list2):
            if name in index1:
                total = index1[name] + j
                
                if total < min_sum:
                    # Новый минимум — сбрасываем результат
                    min_sum = total
                    result = [name]
                elif total == min_sum:
                    # Такая же сумма — добавляем
                    result.append(name)
        
        return result
