"""
Same Tree.
LeetCode #100, Easy.

Дано: корни двух бинарных деревьев p и q.
Вернуть: true если деревья одинаковы.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        Итеративный DFS с явным стеком.
        
        Безопаснее рекурсии: стек в куче, нет риска RecursionError
        на вырожденном дереве (цепочке из 10⁴ узлов).
        Память O(h) — высота дерева, элементы стека ~16 байт.
        """
        stack = [(p, q)]
        
        while stack:
            a, b = stack.pop()
            
            # Оба None — эта ветка одинакова
            if not a and not b:
                continue
            
            # Структура разная ИЛИ значения разные
            if not a or not b or a.val != b.val:
                return False
            
            # Добавляем детей для сравнения
            stack.append((a.left, b.left))
            stack.append((a.right, b.right))
        
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
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [], True),
        ([0], [0], True),
    ]
    
    for p_vals, q_vals, expected in tests:
        p = build_tree(p_vals)
        q = build_tree(q_vals)
        result = sol.isSameTree(p, q)
        status = "✓" if result == expected else "✗"
        print(f"{status} p={p_vals}, q={q_vals} → {result} (ожидалось {expected})")
