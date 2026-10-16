class Solution:
    def preorder(self, root) -> list[int]:
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push детей в ОБРАТНОМ порядке
            # Первый ребёнок окажется наверху стека → выйдет первым
            for child in reversed(node.children):
                stack.append(child)
        
        return result
