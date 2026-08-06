class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Два указателя: слева и справа
        left, right = 0, len(s) - 1
        
        while left < right:
            # Пропускаем не-буквоцифры слева
            # isalnum() — True для букв и цифр
            while left < right and not s[left].isalnum():
                left += 1
            
            # Пропускаем не-буквоцифры справа
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Сравниваем символы без учёта регистра
            if s[left].lower() != s[right].lower():
                return False
            
            # Двигаемся к центру
            left += 1
            right -= 1
        
        return True
