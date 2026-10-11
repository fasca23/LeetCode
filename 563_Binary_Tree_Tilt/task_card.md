---
id: binary-tree-tilt
title: 563. Наклон бинарного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-tree-tilt/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/563_Binary_Tree_Tilt
description: Дано бинарное дерево. Наклон узла = |сумма левого - сумма правого|. Общий наклон = сумма наклонов всех узлов. DFS: возвращаем сумму поддерева, накапливаем наклон.
screenshots: 0
---

**Подход: Post-order DFS**

1. **Идея:** Для каждого узла считаем сумму левого и правого поддеревьев. Наклон = |left_sum - right_sum|. Суммируем все наклоны.
2. **Логика:** `total_tilt = 0`. DFS(node): возвращает сумму поддерева. `left_sum = dfs(node.left)`, `right_sum = dfs(node.right)`. `total_tilt += abs(left_sum - right_sum)`. Вернуть `node.val + left_sum + right_sum`.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек рекурсии.

**Ключевой момент:** Наклон считается по СУММЕ значений, не по высоте. Возвращаем сумму наверх, наклон накапливаем.
