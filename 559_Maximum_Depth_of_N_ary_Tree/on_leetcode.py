class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        
        max_depth = 0
        # Стек: (узел, глубина)
        stack = [(root, 1)]
        
        while stack:
            node, depth = stack.pop()
            
            # Обновляем максимум
            if depth > max_depth:
                max_depth = depth
            
            # Добавляем всех детей с глубиной +1
            for child in node.children:
                stack.append((child, depth + 1))
        
        return max_depth
