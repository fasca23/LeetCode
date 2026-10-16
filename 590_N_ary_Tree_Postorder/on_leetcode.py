class Solution:
    def postorder(self, root) -> list[int]:
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push детей в ПРЯМОМ порядке (не обратном!)
            for child in node.children:
                stack.append(child)
        
        # Reverse даёт postorder
        return result[::-1]
