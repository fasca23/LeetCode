---
id: remove-nth-node-from-end-of-list
title: 19. Удалить N-й узел с конца списка
difficulty: Medium
leetcode_url: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/19_Remove_Nth_Node
description: Дан связный список. Удалить N-й узел с конца. Два указателя: fast идёт на N шагов вперёд, потом оба идут до конца. slow окажется перед удаляемым.
screenshots: 0
---

**Подход: Два указателя (fast и slow)**

1. **Идея:** fast идёт на N шагов вперёд. Затем оба идут одновременно. Когда fast дойдёт до конца — slow стоит перед удаляемым узлом.
2. **Логика:** `dummy = ListNode(0, head)`. `fast = slow = dummy`. Сначала fast делает N+1 шагов. Потом оба идут пока fast не None. `slow.next = slow.next.next`.
3. **Время:** O(n) — один проход.
4. **Память:** O(1).

**Ключевой момент:** dummy-узел решает проблему удаления головы. fast делает N+1 шагов чтобы slow оказался ПЕРЕД удаляемым.
