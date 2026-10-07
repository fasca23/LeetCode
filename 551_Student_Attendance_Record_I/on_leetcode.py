class Solution:
    def checkRecord(self, s: str) -> bool:
        count_a = 0      # общее количество отсутствий
        count_l = 0      # текущая серия опозданий
        max_l = 0        # максимальная серия опозданий
        
        for ch in s:
            if ch == 'A':
                count_a += 1
                count_l = 0  # серия L прервана
            elif ch == 'L':
                count_l += 1
                if count_l > max_l:
                    max_l = count_l
            else:  # 'P'
                count_l = 0  # серия L прервана
        
        # Меньше 2 отсутствий И нет 3 опозданий подряд
        return count_a < 2 and max_l < 3
