---
id: second-minimum-node-in-a-binary-tree
title: 671. Второе минимальное значение в бинарном дереве
difficulty: Easy
leetcode_url: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/671_Second_Minimum_Node
description: Дано специальное дерево: каждый узел ≤ детей. Найти второе минимальное уникальное значение. Корень = минимум. DFS: ищем минимальное > корня.
screenshots: 0
---

**Подход: DFS с поиском второго минимума**

1. **Идея:** В специальном дереве корень — минимум. Ищем минимальное значение строго больше корня.
2. **Логика:** `first = root.val`. `second = inf`. DFS со стеком: для каждого узла если `first < node.val < second` → `second = node.val`. Если `second == inf` → -1, иначе second.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек.

**Ключевой момент:** Свойство дерева: родитель ≤ детей. Корень — глобальный минимум. Второй минимум — минимальное значение строго больше корня.
