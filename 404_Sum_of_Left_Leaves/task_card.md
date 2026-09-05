---
id: sum-of-left-leaves
title: 404. Сумма левых листьев
difficulty: Easy
leetcode_url: https://leetcode.com/problems/sum-of-left-leaves/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/404_Sum_of_Left_Leaves
description: Дано бинарное дерево. Найти сумму всех левых листьев (узел без детей, который является левым ребёнком). DFS со стеком: храним (узел, is_left).
screenshots: 0
---

**Подход: DFS со стеком**

1. **Идея:** Обходим дерево в глубину. Для каждого узла храним флаг is_left. Если узел — лист (нет детей) и is_left — добавляем его значение к сумме.
2. **Логика:** `stack = [(root, False)]`. Пока стек: `node, is_left = stack.pop()`. Если лист и is_left → `total += node.val`. Иначе добавить детей: левого с True, правого с False.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек в куче.

**Ключевой момент:** Левый лист = узел без детей И левый ребёнок. Правые листья не считаются.
