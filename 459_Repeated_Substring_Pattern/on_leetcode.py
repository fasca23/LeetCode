class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Удваиваем строку, убираем первый и последний символ
        # Если s — повтор подстроки, то s найдётся внутри
        doubled = (s + s)[1:-1]
        return s in doubled
