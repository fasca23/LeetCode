class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        
        # Считаем высоту левого края (идём только влево)
        left_h = 0
        node = root.left
        while node:
            left_h += 1
            node = node.left
        
        # Считаем высоту правого края (идём только влево от правого)
        right_h = 0
        node = root.right
        while node:
            right_h += 1
            node = node.left
        
        # Если высоты равны — левое поддерево ПОЛНОЕ
        # 2^left_h узлов + корень + рекурсивно правое
        if left_h == right_h:
            return (1 << left_h) + self.countNodes(root.right)
        else:
            # Иначе правое поддерево полно на уровень меньше
            return (1 << right_h) + self.countNodes(root.left)
