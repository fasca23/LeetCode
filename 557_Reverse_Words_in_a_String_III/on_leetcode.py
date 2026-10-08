class Solution:
    def reverseWords(self, s: str) -> str:
        # Разбиваем по пробелам
        words = s.split(' ')
        
        # Разворачиваем каждое слово
        reversed_words = [word[::-1] for word in words]
        
        # Склеиваем обратно через пробел
        return ' '.join(reversed_words)
