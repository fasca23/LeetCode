class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            # Высоты поддеревьев
            left_h = height(node.left)
            right_h = height(node.right)
            
            # Диаметр через текущий узел
            self.diameter = max(self.diameter, left_h + right_h)
            
            # Высота узла для родителя
            return 1 + max(left_h, right_h)
        
        height(root)
        return self.diameter
