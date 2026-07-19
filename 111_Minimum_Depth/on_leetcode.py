class Solution:
    def minDepth(self, root) -> int:
        # Пустое дерево — глубина 0
        if not root:
            return 0
        
        # BFS с очередью: (узел, глубина)
        # deque — двусторонняя очередь, popleft() за O(1)
        from collections import deque
        queue = deque([(root, 1)])
        
        while queue:
            # Берём из начала очереди (FIFO — первый зашёл, первый вышел)
            node, depth = queue.popleft()
            
            # Проверяем: это лист? (нет обоих детей)
            if not node.left and not node.right:
                # Первый встреченный лист → минимальная глубина
                return depth
            
            # Добавляем детей в конец очереди
            # Они будут обработаны на следующих итерациях
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        # Сюда не дойдём, но для полноты
        return 0
