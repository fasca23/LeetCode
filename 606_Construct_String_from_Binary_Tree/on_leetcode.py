class Solution:
    def tree2str(self, root) -> str:
        if not root:
            return ""
        
        s = str(root.val)
        
        # Левый ребёнок — всегда в скобках
        if root.left:
            s += "(" + self.tree2str(root.left) + ")"
        # Правый есть, левого нет — нужны пустые скобки
        elif root.right:
            s += "()"
        
        # Правый ребёнок
        if root.right:
            s += "(" + self.tree2str(root.right) + ")"
        
        return s
