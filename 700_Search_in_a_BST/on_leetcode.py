class Solution:
    def searchBST(self, root, val: int):
        current = root
        
        while current:
            if val == current.val:
                # Нашли — возвращаем поддерево
                return current
            elif val < current.val:
                # Ищем левее
                current = current.left
            else:
                # Ищем правее
                current = current.right
        
        # Не нашли
        return None
