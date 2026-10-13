---
id: subtree-of-another-tree
title: 572. Поддерево другого дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/subtree-of-another-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/572_Subtree_of_Another_Tree
description: Даны два дерева root и subRoot. Проверить, является ли subRoot поддеревом root. Обходим root, для каждого узла проверяем совпадение с subRoot (isSameTree).
screenshots: 0
---

**Подход: DFS + проверка идентичности**

1. **Идея:** Обходим root. Для каждого узла вызываем isSameTree(node, subRoot). Если совпало — True.
2. **Логика:** `if not root: return False`. `if isSameTree(root, subRoot): return True`. `return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)`.
3. **Время:** O(n × m) — для каждого узла root проверка subRoot.
4. **Память:** O(h) — стек рекурсии.

**Ключевой момент:** isSameTree — вспомогательная функция из задачи 100. Проверяет полное совпадение двух деревьев.
