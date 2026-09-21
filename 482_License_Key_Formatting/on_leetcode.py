class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Убираем дефисы и переводим в верхний регистр
        s = s.replace('-', '').upper()
        
        result = []
        # Идём с конца, набираем группы по k
        for i in range(len(s), 0, -k):
            # Берём срез длиной k (первая группа может быть короче)
            result.append(s[max(0, i - k):i])
        
        # Собираем с дефисами, разворачиваем (собирали с конца)
        return '-'.join(reversed(result))
