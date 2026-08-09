class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        # Итеративный DFS со стеком
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            # Меняем местами левого и правого ребёнка
            # Python: можно в одну строку без временной переменной
            node.left, node.right = node.right, node.left
            
            # Добавляем детей в стек (порядок не важен)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root
