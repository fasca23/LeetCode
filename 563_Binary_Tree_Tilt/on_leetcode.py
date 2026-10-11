class Solution:
    def findTilt(self, root) -> int:
        self.total_tilt = 0
        
        def dfs(node):
            if not node:
                return 0
            
            # Суммы поддеревьев
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            # Наклон текущего узла
            self.total_tilt += abs(left_sum - right_sum)
            
            # Возвращаем сумму поддерева с этим узлом
            return node.val + left_sum + right_sum
        
        dfs(root)
        return self.total_tilt
