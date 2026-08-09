---
id: invert-binary-tree
title: 226. Инвертировать бинарное дерево
difficulty: Easy
leetcode_url: https://leetcode.com/problems/invert-binary-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/226_Invert_Binary_Tree
description: Дано бинарное дерево. Инвертировать его — поменять местами левых и правых детей для всех узлов. Рекурсивно или итеративно со стеком: меняем left/right местами.
screenshots: 0
---

**Подход: Итеративный DFS со стеком**

1. **Идея:** Для каждого узла меняем местами левого и правого ребёнка. Обходим дерево в глубину со стеком.
2. **Логика:** `stack = [root]`. Пока стек: `node = stack.pop()`. Поменять местами `node.left` и `node.right`. Добавить детей в стек.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек в куче, высота дерева.

**Ключевой момент:** Порядок обхода не важен (pre/post/in) — результат одинаков. Менять можно на любом этапе.
