class Solution:
    def getMinimumDifference(self, root) -> int:
        min_diff = float('inf')
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
            
            # Сравниваем с предыдущим (соседним в отсортированном порядке)
            if prev is not None:
                diff = current.val - prev
                if diff < min_diff:
                    min_diff = diff
            
            prev = current.val
            current = current.right
        
        return min_diff
