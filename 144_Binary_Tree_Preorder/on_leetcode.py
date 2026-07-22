class Solution:
    def preorderTraversal(self, root) -> list[int]:
        # Preorder: корень → левое → правое
        result = []
        
        if not root:
            return result
        
        # Стек для итеративного обхода (вместо рекурсии)
        # Кладём корень первым
        stack = [root]
        
        while stack:
            # Берём верхний узел — это текущий "корень"
            node = stack.pop()
            result.append(node.val)
            
            # Порядок push важен:
            # Сначала ПРАВЫЙ — он выйдет ПОЗЖЕ
            if node.right:
                stack.append(node.right)
            # Потом ЛЕВЫЙ — он выйдет ПЕРВЫМ (LIFO)
            if node.left:
                stack.append(node.left)
        
        return result
