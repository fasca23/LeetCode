class Solution:
    def findSecondMinimumValue(self, root) -> int:
        if not root:
            return -1
        
        first = root.val  # минимум
        second = float('inf')  # второй минимум
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            # Ищем минимальное значение строго больше first
            if first < node.val < second:
                second = node.val
            
            # Оптимизация: не идём в детей если значение >= second
            # (только если second уже найден)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return second if second != float('inf') else -1
