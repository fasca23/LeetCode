"""
Median of Two Sorted Arrays.
LeetCode #4, Hard.

Дано: два отсортированных массива nums1, nums2.
Вернуть: медиану объединения за O(log(min(n, m))).
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Бинарный поиск по меньшему массиву.
        
        Делим оба массива так, чтобы левая половина содержала
        ровно половину всех элементов, и max(левой) ≤ min(правой).
        """
        # nums1 должен быть короче — так быстрее
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2  # сколько элементов должно быть слева
        
        left, right = 0, m  # бинарный поиск по nums1
        
        while True:
            # mid1 — сколько элементов из nums1 берём в левую часть
            mid1 = (left + right) // 2
            # Остальные добираем из nums2
            mid2 = half - mid1
            
            # Граничные элементы левой и правой частей
            # float('-inf') / float('inf') — если часть пустая
            l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < m else float('inf')
            l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = nums2[mid2] if mid2 < n else float('inf')
            
            # Проверяем: разбиение корректно?
            if l1 <= r2 and l2 <= r1:
                # Нашли правильное разбиение
                if total % 2 == 1:
                    # Нечётное — медиана в правой части
                    return float(min(r1, r2))
                else:
                    # Чётное — среднее max левой и min правой
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                # nums1 даёт слишком много элементов слева
                right = mid1 - 1
            else:
                # nums1 даёт слишком мало элементов слева
                left = mid1 + 1


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1, 3, 8], [7, 9, 10, 11], 8.0),
    ]
    
    for nums1, nums2, expected in tests:
        result = sol.findMedianSortedArrays(nums1, nums2)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums1={nums1!s:15} nums2={nums2!s:15} → {result} (ожидалось {expected})")
