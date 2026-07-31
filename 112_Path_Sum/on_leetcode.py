class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        # Пустое дерево — пути нет
        if not root:
            return False
        
        # Стек: (узел, оставшаяся сумма)
        # Оставшаяся сумма = targetSum минус значения на пути
        stack = [(root, targetSum - root.val)]
        
        while stack:
            node, remain = stack.pop()
            
            # Проверяем: это лист и сумма совпала?
            if not node.left and not node.right and remain == 0:
                return True
            
            # Идём вправо: вычитаем значение правого ребёнка
            if node.right:
                stack.append((node.right, remain - node.right.val))
            
            # Идём влево: вычитаем значение левого ребёнка
            if node.left:
                stack.append((node.left, remain - node.left.val))
        
        # Ни один путь не дал нужную сумму
        return False
