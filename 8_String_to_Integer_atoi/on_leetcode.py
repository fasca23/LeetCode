class Solution:
    def myAtoi(self, s: str) -> int:
        # Границы 32-битного целого
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        n = len(s)
        i = 0
        
        # Шаг 1: пропускаем ведущие пробелы
        while i < n and s[i] == ' ':
            i += 1
        
        # Если строка кончилась или только пробелы
        if i == n:
            return 0
        
        # Шаг 2: определяем знак
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Шаг 3: считываем цифры
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Проверка переполнения ДО умножения
            # result * 10 + digit > INT_MAX ?
            if result > (INT_MAX - digit) // 10:
                return INT_MIN if sign == -1 else INT_MAX
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
