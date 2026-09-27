class Solution:
    def findMode(self, root) -> list[int]:
        if not root:
            return []
        
        result = []
        max_count = 0
        count = 0
        prev = None
        
        # Inorder обход со стеком
        stack = []
        current = root
        
        while current or stack:
            # Идём максимально влево
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            
            # Считаем серию одинаковых значений
            if prev is not None and current.val == prev:
                count += 1
            else:
                count = 1
            
            # Обновляем максимум и список мод
            if count > max_count:
                max_count = count
                result = [current.val]
            elif count == max_count:
                result.append(current.val)
            
            prev = current.val
            current = current.right
        
        return result
