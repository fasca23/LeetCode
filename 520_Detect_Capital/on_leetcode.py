class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Три допустимых случая:
        # 1. Все строчные: "hello"
        # 2. Все заглавные: "HELLO"
        # 3. Только первая заглавная: "Hello"
        return word.islower() or word.isupper() or word.istitle()
