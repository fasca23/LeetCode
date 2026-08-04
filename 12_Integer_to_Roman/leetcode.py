class Solution:
    def intToRoman(self, num: int) -> str:
        # Таблица всех номиналов от большего к меньшему
        # Включаем составные (CM, CD, XC, XL, IX, IV)
        # чтобы не было более 3 одинаковых символов подряд
        values = [
            (1000, "M"), (900, "CM"),
            (500, "D"),  (400, "CD"),
            (100, "C"),  (90, "XC"),
            (50, "L"),   (40, "XL"),
            (10, "X"),   (9, "IX"),
            (5, "V"),    (4, "IV"),
            (1, "I")
        ]
        
        result = ""
        
        for value, symbol in values:
            # Пока можем вычесть номинал — вычитаем и добавляем символ
            while num >= value:
                num -= value
                result += symbol
        
        return result
