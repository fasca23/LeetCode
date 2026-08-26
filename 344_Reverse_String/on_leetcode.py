class Solution:
    def reverseString(self, s: list[str]) -> None:
        # Два указателя: слева и справа
        left, right = 0, len(s) - 1
        
        # Меняем местами пока не встретились в центре
        while left < right:
            # Обмен: левый и правый символы
            s[left], s[right] = s[right], s[left]
            
            # Двигаемся к центру
            left += 1
            right -= 1
