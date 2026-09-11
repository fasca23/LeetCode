class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        # Таблица: цифра → буквы
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, path):
            # Дошли до конца — комбинация готова
            if index == len(digits):
                result.append(path)
                return
            
            # Перебираем все буквы для текущей цифры
            for ch in phone[digits[index]]:
                backtrack(index + 1, path + ch)
        
        backtrack(0, "")
        return result
