"""
Maximum Depth of Binary Tree.
LeetCode #104, Easy.

Дано: корень бинарного дерева.
Вернуть: максимальную глубину (число узлов от корня до листа).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        Итеративный DFS с явным стеком.
        
        Храним пары (узел, глубина). На каждом шаге
        обновляем максимум. Стек в куче — без риска RecursionError.
        """
        if not root:
            return 0
        
        max_depth = 0
        stack = [(root, 1)]  # (узел, текущая глубина)
        
        while stack:
            node, depth = stack.pop()
            
            # Обновляем максимум
            if depth > max_depth:
                max_depth = depth
            
            # Детей добавляем с глубиной +1
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_depth


# ------------------------ Помощники ------------------------

from collections import deque

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([1], 1),
        ([1, 2, 3, 4, 5, 6, 7], 3),
    ]
    
    for values, expected in tests:
        root = build_tree(values)
        result = sol.maxDepth(root)
        status = "✓" if result == expected else "✗"
        print(f"{status} {values} → {result} (ожидалось {expected})")
