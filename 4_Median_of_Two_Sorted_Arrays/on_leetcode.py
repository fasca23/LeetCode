class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        left, right = 0, m
        
        while True:
            mid1 = (left + right) // 2
            mid2 = half - mid1
            
            l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < m else float('inf')
            l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = nums2[mid2] if mid2 < n else float('inf')
            
            if l1 <= r2 and l2 <= r1:
                if total % 2:
                    return float(min(r1, r2))
                return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                right = mid1 - 1
            else:
                left = mid1 + 1
