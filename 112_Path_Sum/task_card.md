---
id: path-sum
title: 112. Сумма пути
difficulty: Easy
leetcode_url: https://leetcode.com/problems/path-sum/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/112_Path_Sum
description: Дано бинарное дерево и число targetSum. Проверить, существует ли путь от корня до листа с суммой равной targetSum. DFS со стеком: идём вглубь, вычитаем значения узлов из targetSum.
screenshots: 0
---

**Подход: DFS со стеком**

1. **Идея:** Идём от корня к листьям. На каждом шаге вычитаем значение узла из targetSum. Если дошли до листа и остаток = 0 — путь найден.
2. **Логика:** `stack = [(root, targetSum - root.val)]`. Пока стек: `node, remain = stack.pop()`. Если лист и `remain == 0` → True. Иначе добавить детей с `remain - child.val`.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек в куче, высота дерева.

**Ключевой момент:** Лист = узел без обоих детей. Путь ОБЯЗАТЕЛЬНО от корня до листа, не до середины.
