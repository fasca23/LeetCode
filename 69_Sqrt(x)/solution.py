"""
Sqrt(x).
LeetCode #69, Easy.

Дано: целое неотрицательное x.
Вернуть: квадратный корень из x, округлённый вниз.
Без встроенных функций возведения в степень.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Бинарный поиск.
        
        Ищем наибольшее целое число, квадрат которого <= x.
        Диапазон: [0, x]. Особый случай: x = 0 или 1.
        """
        if x < 2:
            return x
        
        left, right = 1, x
        
        while left <= right:
            mid = (left + right) // 2
            
            # Сравниваем mid * mid с x
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # Когда left > right, right — последнее число, чей квадрат < x
        return right


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        (4, 2),
        (8, 2),
        (0, 0),
        (1, 1),
        (2, 1),
        (10, 3),
        (16, 4),
    ]
    
    for x, expected in tests:
        result = sol.mySqrt(x)
        status = "✓" if result == expected else "✗"
        print(f"{status} x={x:3} → {result} (ожидалось {expected})")
