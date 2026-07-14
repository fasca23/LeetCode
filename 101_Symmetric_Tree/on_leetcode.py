class Solution:
    def isSymmetric(self, root) -> bool:
        """
        DFS со стеком (в куче).
        
        Сравниваем левое и правое поддеревья перекрёстно.
        Стек в куче → не падает на цепочке (в отличие от рекурсии).
        Память O(h), время O(n).
        """
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        
        while stack:
            a, b = stack.pop()
            
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            
            # Перекрёстно: левый-левый с правым-правым, левый-правый с правым-левым
            stack.append((a.left, b.right))
            stack.append((a.right, b.left))
        
        return True
