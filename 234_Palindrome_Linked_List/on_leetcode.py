class Solution:
    def isPalindrome(self, head) -> bool:
        # Находим середину: slow 1 шаг, fast 2 шага
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Разворачиваем вторую половину
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Сравниваем первую половину с развёрнутой второй
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
