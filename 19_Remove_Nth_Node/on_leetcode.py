class Solution:
    def removeNthFromEnd(self, head, n: int):
        # Фиктивный узел перед головой
        dummy = ListNode(0)
        dummy.next = head
        
        # Оба указателя начинают с dummy
        fast = slow = dummy
        
        # fast идёт на n+1 шагов вперёд
        # n+1 чтобы slow оказался ПЕРЕД удаляемым
        for _ in range(n + 1):
            fast = fast.next
        
        # Оба идут пока fast не дойдёт до конца
        while fast:
            fast = fast.next
            slow = slow.next
        
        # slow теперь перед удаляемым узлом
        slow.next = slow.next.next
        
        return dummy.next
