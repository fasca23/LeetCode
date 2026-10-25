class Solution:
    def mergeTrees(self, root1, root2):
        # Одно дерево пустое — возвращаем другое
        if not root1:
            return root2
        if not root2:
            return root1
        
        # Оба есть — складываем значения
        root1.val += root2.val
        
        # Рекурсивно сливаем левых и правых детей
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1
