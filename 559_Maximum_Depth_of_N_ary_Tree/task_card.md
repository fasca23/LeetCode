---
id: maximum-depth-of-n-ary-tree
title: 559. Максимальная глубина N-арного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/559_Maximum_Depth_of_N_ary_Tree
description: Дано N-арное дерево (у каждого узла любое число детей). Найти максимальную глубину. DFS со стеком: храним (узел, глубина), обновляем максимум.
screenshots: 0
---

**Подход: DFS со стеком**

1. **Идея:** Как в 104 (Maximum Depth of Binary Tree), но у узла список children вместо left/right.
2. **Логика:** `stack = [(root, 1)]`. Пока стек: `node, depth = stack.pop()`. Обновить max_depth. Для каждого child: `stack.append((child, depth + 1))`.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек в куче.

**Ключевой момент:** Дети хранятся в списке `node.children`. Обходим циклом.
