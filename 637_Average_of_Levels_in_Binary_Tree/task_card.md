---
id: average-of-levels-in-binary-tree
title: 637. Среднее по уровням бинарного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/637_Average_of_Levels_in_Binary_Tree
description: Дано бинарное дерево. Вернуть среднее значение узлов на каждом уровне. BFS с очередью: на каждом уровне считаем сумму и количество.
screenshots: 0
---

**Подход: BFS с очередью**

1. **Идея:** Обходим дерево по уровням. Для каждого уровня считаем сумму и количество узлов, делим.
2. **Логика:** `queue = deque([root])`. Пока очередь: `level_size = len(queue)`, `level_sum = 0`. Для _ в range(level_size): `node = popleft()`, `level_sum += node.val`, добавить детей. `result.append(level_sum / level_size)`.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(w) — ширина дерева.

**Ключевой момент:** `level_size = len(queue)` фиксирует количество узлов на текущем уровне до добавления детей следующего.
