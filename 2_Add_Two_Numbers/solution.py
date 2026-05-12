"""Решение задачи Add Two Numbers с LeetCode."""


class ListNode:
    """Узел односвязного списка."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Сложение двух чисел в связных списках.
    Цифры хранятся от младшей к старшей: 342 → [2,4,3]
    """
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # фиктивная голова для удобства
        current = dummy
        carry = 0             # перенос в следующий разряд
        
        # Идём пока есть узлы или перенос
        while l1 or l2 or carry:
            # Берём цифру или 0, если список кончился
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Считаем сумму с переносом
            total = v1 + v2 + carry
            carry = total // 10      # новый перенос
            digit = total % 10       # цифра для записи
            
            # Добавляем узел в результат
            current.next = ListNode(digit)
            current = current.next
            
            # Шагаем дальше
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next


# ------------------------ Помощники ------------------------

def to_list(head):
    """Связный список → Python-список."""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def to_linked(arr):
    """Python-список → связный список."""
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    # 342 + 465 = 807
    l1 = to_linked([2, 4, 3])
    l2 = to_linked([5, 6, 4])
    res = sol.addTwoNumbers(l1, l2)
    print(f"[2,4,3] + [5,6,4] = {to_list(res)}")  # [7, 0, 8]
    
    # 999 + 1 = 1000
    l1 = to_linked([9, 9, 9])
    l2 = to_linked([1])
    res = sol.addTwoNumbers(l1, l2)
    print(f"[9,9,9] + [1] = {to_list(res)}")        # [0, 0, 0, 1]