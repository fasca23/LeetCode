class Solution:
    def binaryTreePaths(self, root) -> list[str]:
        if not root:
            return []
        
        result = []
        # Стек: (узел, путь до этого узла)
        stack = [(root, str(root.val))]
        
        while stack:
            node, path = stack.pop()
            
            # Если лист — путь завершён
            if not node.left and not node.right:
                result.append(path)
            
            # Правый ребёнок
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            
            # Левый ребёнок
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
        
        return result
