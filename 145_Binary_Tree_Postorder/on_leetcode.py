class Solution:
    def postorderTraversal(self, root) -> list[int]:
        # Postorder: левое → правое → корень
        result = []
        
        if not root:
            return result
        
        # Стек хранит (узел, посетили_детей?)
        # visited=False → первый раз, нужно обработать детей
        # visited=True  → второй раз, дети готовы
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            
            if visited:
                # Второй раз: оба ребёнка уже обработаны
                # Добавляем текущий узел в результат
                result.append(node.val)
            else:
                # Первый раз: кладём обратно с пометкой
                stack.append((node, True))
                
                # Кладём детей: сначала правый, потом левый
                # Левый выйдет первым (LIFO) → обработается раньше
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        
        return result
