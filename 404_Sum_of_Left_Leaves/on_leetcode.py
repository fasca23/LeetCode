class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return 0
        
        total = 0
        # Стек: (узел, является ли левым ребёнком)
        stack = [(root, False)]
        
        while stack:
            node, is_left = stack.pop()
            
            # Проверяем: это лист и левый?
            if not node.left and not node.right and is_left:
                total += node.val
            
            # Правый ребёнок — не левый
            if node.right:
                stack.append((node.right, False))
            
            # Левый ребёнок — левый
            if node.left:
                stack.append((node.left, True))
        
        return total
