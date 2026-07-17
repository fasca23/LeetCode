"""
Balanced Binary Tree.
LeetCode #110, Easy.

Дано: корень бинарного дерева.
Вернуть: true если дерево сбалансировано (разница высот ≤ 1 для всех узлов).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        Итеративный DFS с явным стеком и пост-обработкой.
        
        Обходим дерево, вычисляем высоты снизу вверх.
        Если разница > 1 — возвращаем -1 как флаг дисбаланса.
        Стек в куче — без риска RecursionError.
        """
        if not root:
            return True
        
        # Стек для post-order: (узел, посетили_детей?)
        stack = [(root, False)]
        heights = {}  # узел → высота его поддерева (None → 0)
        heights[None] = 0
        
        while stack:
            node, visited = stack.pop()
            
            if not visited:
                # Первый раз — кладём обратно с пометкой и добавляем детей
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
            else:
                # Второй раз — дети уже обработаны
                left_h = heights[node.left]
                right_h = heights[node.right]
                
                # Проверяем баланс
                if abs(left_h - right_h) > 1:
                    return False
                
                # Сохраняем высоту текущего узла
                heights[node] = 1 + max(left_h, right_h)
        
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
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([], True),
        ([1], True),
        ([1, 2, None, 3], False),
    ]
    
    for values, expected in tests:
        root = build_tree(values)
        result = sol.isBalanced(root)
        status = "✓" if result == expected else "✗"
        print(f"{status} {values} → {result} (ожидалось {expected})")
