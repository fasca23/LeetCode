"""
Symmetric Tree.
LeetCode #101, Easy.

Дано: корень бинарного дерева.
Вернуть: true если дерево симметрично (зеркальное отражение).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        """
        Итеративный DFS с явным стеком.
        
        Сравниваем левое и правое поддеревья перекрёстно:
        (left.left, right.right) и (left.right, right.left).
        Стек в куче — не упадёт на вырожденном дереве.
        """
        if not root:
            return True  # пустое дерево симметрично
        
        stack = [(root.left, root.right)]
        
        while stack:
            a, b = stack.pop()
            
            # Оба None — эта ветка симметрична
            if not a and not b:
                continue
            
            # Структура разная ИЛИ значения разные
            if not a or not b or a.val != b.val:
                return False
            
            # Перекрёстное добавление — в этом суть зеркальности
            stack.append((a.left, b.right))   # левый-левый ↔ правый-правый
            stack.append((a.right, b.left))   # левый-правый ↔ правый-левый
        
        return True


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
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        ([1, 2, 2, None, 3, 3], True),
        ([], True),
        ([1], True),
        ([1, 2], False),
    ]
    
    for values, expected in tests:
        root = build_tree(values)
        result = sol.isSymmetric(root)
        status = "✓" if result == expected else "✗"
        print(f"{status} {values} → {result} (ожидалось {expected})")
