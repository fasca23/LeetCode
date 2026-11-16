class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if letters[mid] <= target:
                # Ищем правее
                left = mid + 1
            else:
                # Запоминаем, но ищем левее (может есть меньше)
                right = mid - 1
        
        # left — первая буква > target, или len (тогда циклично → 0)
        return letters[left % len(letters)]
