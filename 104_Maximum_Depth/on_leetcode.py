class Solution:
    def maxDepth(self, root) -> int:
        """
        DFS со стеком (в куче).
        Храним (узел, глубина). Обновляем максимум.
        Стек в куче → не падает на цепочке.
        Время O(n), память O(h).
        """
        if not root:
            return 0
        
        max_depth = 0
        stack = [(root, 1)]
        
        while stack:
            node, depth = stack.pop()
            
            if depth > max_depth:
                max_depth = depth
            
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_depth
