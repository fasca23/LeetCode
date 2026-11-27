class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        # Таблица Морзе для a-z (26 кодов)
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]
        
        seen = set()
        
        for word in words:
            # Собираем код Морзе: каждая буква → код, склеиваем
            code = ''.join(morse[ord(ch) - ord('a')] for ch in word)
            seen.add(code)
        
        return len(seen)
