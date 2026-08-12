---
id: implement-queue-using-stacks
title: 232. Реализация очереди через стеки
difficulty: Easy
leetcode_url: https://leetcode.com/problems/implement-queue-using-stacks/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/232_Implement_Queue_using_Stacks
description: Реализовать очередь (FIFO) используя два стека (LIFO). Входной стек для push, выходной для pop/peek. Если выходной пуст — перекладываем всё из входного.
screenshots: 0
---

**Подход: Два стека**

1. **Идея:** Очередь = FIFO, стек = LIFO. Два стека: входной (push) и выходной (pop). Когда нужен pop/peek и выходной пуст — перекладываем всё из входного. Порядок разворачивается.
2. **Логика:** `push(x)`: добавить во входной стек. `pop()`: если выходной пуст — переложить все элементы из входного в выходной. `pop()` с выходного. `peek()` аналогично.
3. **Время:** push O(1), pop/peek — амортизированное O(1).
4. **Память:** O(n) — два стека.

**Ключевой момент:** Перекладывание разворачивает порядок. Двойной разворот = исходный порядок (FIFO).
