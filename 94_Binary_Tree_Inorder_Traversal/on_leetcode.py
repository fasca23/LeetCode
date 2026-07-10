class Solution:
    def inorderTraversal(self, root):
        result = []          # сюда складываем ответ (значения по порядку)
        stack = []           # стек для хранения узлов "на потом"
        current = root       # начинаем с корня
        
        # Пока есть куда идти (current) или есть что доставать (stack)
        while current or stack:
            
            # === Фаза 1: идём максимально влево ===
            # Пока есть узел — кладём его в стек и идём в левого ребёнка
            while current:
                stack.append(current)    # запоминаем узел
                current = current.left   # уходим влево
            
            # === Фаза 2: левее некуда — достаём из стека ===
            # Берём верхний узел стека (последний запомненный)
            current = stack.pop()
            
            # Это текущий "корень" — добавляем в результат
            result.append(current.val)
            
            # === Фаза 3: идём вправо ===
            # Правое поддерево обработаем на следующей итерации
            current = current.right
        
        return result
