---
id: minimum-absolute-difference-in-bst
title: 530. Минимальная абсолютная разница в BST
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/530_Minimum_Absolute_Difference_in_BST
description: Дано BST. Найти минимальную разницу между любыми двумя узлами. Inorder-обход даёт отсортированный порядок — минимум всегда между соседями.
screenshots: 0
---

**Подход: Inorder-обход**

1. **Идея:** В BST inorder даёт отсортированные значения. Минимальная разница всегда между соседними элементами в этом порядке.
2. **Логика:** Inorder обход со стеком. Храним prev. Для каждого узла: если prev не None → `min_diff = min(min_diff, node.val - prev)`. Обновляем prev.
3. **Время:** O(n) — один обход.
4. **Память:** O(h) — стек.

**Ключевой момент:** Не нужно сравнивать все пары. В отсортированном порядке минимум всегда между соседями.
