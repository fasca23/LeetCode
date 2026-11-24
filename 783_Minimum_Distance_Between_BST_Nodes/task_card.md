---
id: minimum-distance-between-bst-nodes
title: 783. Минимальное расстояние между узлами BST
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/783_Minimum_Distance_Between_BST_Nodes
description: Дано BST. Найти минимальную разницу между любыми двумя узлами. Inorder-обход даёт отсортированный порядок — минимум между соседями.
screenshots: 0
---

**Подход: Inorder-обход**

1. **Идея:** Как 530 (Minimum Absolute Difference in BST). Inorder даёт отсортированные значения, минимальная разница всегда между соседями.
2. **Логика:** Inorder обход со стеком. `prev = None`. Для каждого узла: если prev не None → `min_diff = min(min_diff, node.val - prev)`. `prev = node.val`.
3. **Время:** O(n) — один обход.
4. **Память:** O(h) — стек.

**Ключевой момент:** В BST inorder = отсортированный порядок. Минимум разницы — между соседними значениями.
