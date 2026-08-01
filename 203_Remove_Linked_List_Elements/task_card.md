---
id: remove-linked-list-elements
title: 203. Удаление элементов из связного списка
difficulty: Easy
leetcode_url: https://leetcode.com/problems/remove-linked-list-elements/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/203_Remove_Linked_List_Elements
description: Дан связный список и значение val. Удалить все узлы со значением val. Фиктивный узел (dummy) перед головой упрощает удаление первого элемента.
screenshots: 0
---

**Подход: Фиктивный узел + один проход**

1. **Идея:** Создаём dummy-узел перед head. Идём по списку: если следующий узел = val → пропускаем его (`current.next = current.next.next`). Иначе переходим дальше.
2. **Логика:** `dummy = ListNode(0, head)`, `cur = dummy`. Пока `cur.next`: если `cur.next.val == val` → `cur.next = cur.next.next`. Иначе `cur = cur.next`. Вернуть `dummy.next`.
3. **Время:** O(n) — один проход.
4. **Память:** O(1) — только указатели.

**Ключевой момент:** dummy-узел решает проблему удаления головы. Без него нужна отдельная проверка первого элемента.
