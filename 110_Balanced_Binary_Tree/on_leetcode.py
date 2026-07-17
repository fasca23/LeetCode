class Solution:
    def isBalanced(self, root) -> bool:
        """
        Итеративный post-order DFS со стеком.
        
        Вычисляем высоты снизу вверх.
        Если разница > 1 → False.
        Стек в куче → без RecursionError.
        Время O(n), память O(h).
        """
        if not root:
            return True
        
        stack = [(root, False)]
        heights = {None: 0}
        
        while stack:
            node, visited = stack.pop()
            
            if not visited:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
            else:
                left_h = heights[node.left]
                right_h = heights[node.right]
                
                if abs(left_h - right_h) > 1:
                    return False
                
                heights[node] = 1 + max(left_h, right_h)
        
        return True
