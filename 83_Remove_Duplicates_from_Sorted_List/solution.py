"""
Remove Duplicates from Sorted List.
LeetCode #83, Easy.

Дано: голова отсортированного связного списка.
Вернуть: голова списка без дубликатов.
"""


class ListNode:
    """Узел односвязного списка."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """
        Один проход по списку.
        
        Идём по списку. Если текущий узел равен следующему —
        пропускаем следующий (меняем ссылку).
        Иначе переходим к следующему.
        """
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Пропускаем дубликат
                current.next = current.next.next
            else:
                # Переходим дальше
                current = current.next
        
        return head


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
    if not arr:
        return None
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


# ------------------------ Демонстрация ------------------------

if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([1, 1, 1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
    ]
    
    for arr, expected in tests:
        head = to_linked(arr)
        result = sol.deleteDuplicates(head)
        result_arr = to_list(result)
        status = "✓" if result_arr == expected else "✗"
        print(f"{status} {arr} → {result_arr} (ожидалось {expected})")
