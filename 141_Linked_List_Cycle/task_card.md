---
id: linked-list-cycle
title: 141. Цикл в связном списке
difficulty: Easy
leetcode_url: https://leetcode.com/problems/linked-list-cycle/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/141_Linked_List_Cycle
description: Дан связный список. Определить, есть ли в нём цикл. Быстрый и медленный указатели (алгоритм Флойда): slow идёт 1 шаг, fast 2 шага. Если встретились — цикл.
screenshots: 0
---

**Подход: Быстрый и медленный указатели (алгоритм Флойда)**

1. **Идея:** slow идёт 1 шаг, fast — 2 шага. Если есть цикл — fast догонит slow (разница сокращается на 1 за итерацию). Если нет — fast дойдёт до None.
2. **Логика:** `slow = head, fast = head`. Пока `fast` и `fast.next`: `slow = slow.next`, `fast = fast.next.next`. Если `slow == fast` → True. Иначе после цикла → False.
3. **Время:** O(n) — fast догонит slow за ≤ n шагов в цикле.
4. **Память:** O(1) — два указателя.

**Ключевой момент:** fast догоняет slow потому что каждый шаг сокращает расстояние между ними на 1 (fast делает 2 шага, slow — 1).
