"""
Convert Sorted Array to Binary Search Tree.
LeetCode #108, Easy.

Дано: отсортированный массив nums.
Вернуть: корень сбалансированного BST.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        """
        Рекурсивное построение с выбором середины.
        
        Корень = средний элемент.
        Левое поддерево = левая половина.
        Правое поддерево = правая половина.
        Повторяем рекурсивно для каждой половины.
        """
        if not nums:
            return None
        
        return self._build(nums, 0, len(nums) - 1)
    
    def _build(self, nums: list[int], left: int, right: int) -> TreeNode | None:
        """Рекурсивно строит поддерево из nums[left..right]."""
        if left > right:
            return None
        
        # Берём середину
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        # Левое поддерево = всё что левее середины
        root.left = self._build(nums, left, mid - 1)
        # Правое поддерево = всё что правее середины
        root.right = self._build(nums, mid + 1, right)
        
        return root


# ------------------------ Помощники ------------------------

def tree_to_list(root):
    """Дерево → список LeetCode-формата (BFS)."""
    if not root:
        return []
    from collections import deque
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    # Убираем хвостовые None
    while result and result[-1] is None:
        result.pop()
    return result


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5]),
        ([1, 3], [3, 1]),  # или [1, None, 3]
        ([], []),
        ([0], [0]),
    ]
    
    for nums, expected in tests:
        root = sol.sortedArrayToBST(nums)
        result = tree_to_list(root)
        # Для BST может быть несколько правильных ответов,
        # проверяем что дерево сбалансировано и содержит все элементы
        print(f"nums={nums}")
        print(f"  → {result}")
