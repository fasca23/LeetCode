---
id: implement-stack-using-queues
title: 225. Реализация стека через очереди
difficulty: Easy
leetcode_url: https://leetcode.com/problems/implement-stack-using-queues/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/225_Implement_Stack_using_Queues
description: Реализовать стек (LIFO) используя только очередь (FIFO). При push перекладываем все элементы после нового в конец — новый оказывается первым.
screenshots: 0
---

**Подход: Одна очередь с перекладыванием**

1. **Идея:** Очередь — FIFO, стек — LIFO. При добавлении элемента кладём его и перекладываем все остальные за ним. Новый элемент становится первым в очереди = верхушкой стека.
2. **Логика:** `push(x)`: добавить x в очередь, затем len-1 раз переложить из начала в конец. `pop()`: popleft(). `top()`: queue[0]. `empty()`: len == 0.
3. **Время:** push O(n), pop O(1), top O(1).
4. **Память:** O(n) — очередь.

**Ключевой момент:** Перекладывание делает новый элемент первым. Очередь хранит элементы в порядке стека (верхушка → дно).
