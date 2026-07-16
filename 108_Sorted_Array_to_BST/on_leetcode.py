class Solution:
    def sortedArrayToBST(self, nums):
        """
        Рекурсия: корень = середина массива.
        Левая половина → левое поддерево.
        Правая половина → правое поддерево.
        
        Сбалансированность гарантирована выбором середины:
        размеры половин отличаются ≤ 1.
        
        Время O(n), память O(log n) — для сбалансированного дерева
        стек рекурсии логарифмический.
        """
        if not nums:
            return None
        return self._build(nums, 0, len(nums) - 1)
    
    def _build(self, nums, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self._build(nums, left, mid - 1)
        root.right = self._build(nums, mid + 1, right)
        
        return root
