class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not root:
            return False
        
        # Проверяем: root и subRoot — одинаковые деревья?
        if self.isSameTree(root, subRoot):
            return True
        
        # Ищем в левом или правом поддереве
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, p, q) -> bool:
        # Оба None — одинаковые
        if not p and not q:
            return True
        # Одно None — разные
        if not p or not q:
            return False
        # Значения равны И поддеревья равны
        return (p.val == q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
