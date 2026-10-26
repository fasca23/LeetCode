class Solution:
    def averageOfLevels(self, root) -> list[float]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            # Количество узлов на текущем уровне
            level_size = len(queue)
            level_sum = 0
            
            # Обрабатываем весь уровень
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Добавляем детей для следующего уровня
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Среднее по уровню
            result.append(level_sum / level_size)
        
        return result
