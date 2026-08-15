---
id: binary-tree-paths
title: 257. Пути бинарного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-tree-paths/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/257_Binary_Tree_Paths
description: Дано бинарное дерево. Вернуть все пути от корня до листьев в формате "1->2->5". DFS со стеком: храним (узел, путь). Если лист — добавляем путь в результат.
screenshots: 0
---

**Подход: DFS со стеком**

1. **Идея:** Обходим дерево в глубину. В стеке храним пары (узел, путь до него). Когда встречаем лист — путь готов, добавляем в результат.
2. **Логика:** `stack = [(root, str(root.val))]`. Пока стек: `node, path = stack.pop()`. Если лист → `result.append(path)`. Иначе добавить детей с `path + "->" + str(child.val)`.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек + O(n) для результата.

**Ключевой момент:** Лист = узел без детей. Путь накапливается как строка в стеке, не нужно восстанавливать обратный путь.
