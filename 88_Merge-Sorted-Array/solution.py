"""
Merge Sorted Array.
LeetCode #88, Easy.

Дано: nums1 (длина m+n, последние n нулей), nums2 (длина n).
Слить nums2 в nums1 на месте, сохранив сортировку.
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Три указателя с конца.
        
        Сравниваем наибольшие элементы nums1 и nums2,
        ставим больший в конец nums1.
        """
        # p — позиция для вставки в nums1 (с конца)
        # p1 — текущий элемент в nums1 (из значимых)
        # p2 — текущий элемент в nums2
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        
        # Пока есть элементы в nums2
        while p2 >= 0:
            # Если в nums1 ещё есть элементы И они больше чем в nums2
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ]
    
    for nums1, m, nums2, n, expected in tests:
        original = nums1[:]
        sol.merge(nums1, m, nums2, n)
        status = "✓" if nums1 == expected else "✗"
        print(f"{status} nums1={original}, m={m}, nums2={nums2}, n={n}")
        print(f"   → {nums1} (ожидалось {expected})")
