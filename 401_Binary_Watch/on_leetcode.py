class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []
        
        # Перебираем все возможные часы (0-11)
        for h in range(12):
            # Перебираем все возможные минуты (0-59)
            for m in range(60):
                # Считаем единичные биты в часах и минутах
                # bin(x).count('1') — количество единиц в двоичной записи
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # Форматируем: часы без ведущего нуля, минуты с ведущим
                    result.append(f"{h}:{m:02d}")
        
        return result
