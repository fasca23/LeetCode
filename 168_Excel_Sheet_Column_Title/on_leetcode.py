class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            # Вычитаем 1: A=1, а не 0
            # Без этого 26 → AZ (неправильно), с вычитанием 26 → Z
            columnNumber -= 1
            
            # Остаток от деления на 26 даёт номер буквы
            # 0→A, 1→B, ..., 25→Z
            letter = chr(ord('A') + columnNumber % 26)
            
            # Добавляем букву в начало (идём от младшего разряда)
            result = letter + result
            
            # Переходим к следующему разряду
            columnNumber //= 26
        
        return result
