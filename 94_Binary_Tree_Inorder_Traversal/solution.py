"""
Binary Tree Inorder Traversal.
LeetCode #94, Easy.

Дано: корень бинарного дерева.
Вернуть: список значений в inorder-обходе (левый → корень → правый).
"""


class TreeNode:
    """Узел бинарного дерева."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        """
        Итеративный обход со стеком.
        
        Идём максимально влево, запоминая узлы в стеке.
        Когда левее некуда — достаём из стека, добавляем в результат,
        идём вправо. Повторяем.
        """
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Идём максимально влево
            while current:
                stack.append(current)
                current = current.left
            
            # Левого поддерева нет — берём из стека
            current = stack.pop()
            result.append(current.val)
            
            # Идём в правое поддерево
            current = current.right
        
        return result


# ------------------------ Помощники ------------------------

def build_tree(values):
    """Строит дерево из списка (LeetCode-формат: [1,null,2,3])."""
    if not values:
        return None
    
    from collections import deque
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
        ([1, None, 2, 3], [1, 3, 2]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [4, 2, 5, 1, 3]),
    ]
    
    for values, expected in tests:
        root = build_tree(values)
        result = sol.inorderTraversal(root)
        status = "✓" if result == expected else "✗"
        print(f"{status} {values} → {result} (ожидалось {expected})")
