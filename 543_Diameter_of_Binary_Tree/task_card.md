---
id: diameter-of-binary-tree
title: 543. Диаметр бинарного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/diameter-of-binary-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/543_Diameter_of_Binary_Tree
description: Дано бинарное дерево. Найти диаметр — длину самого длинного пути между любыми двумя узлами (в рёбрах). DFS: для каждого узла высота = 1 + max(left, right), диаметр через узел = left + right.
screenshots: 0
---

**Подход: DFS с пост-обработкой**

1. **Идея:** Диаметр может проходить через любой узел. Для каждого узла: высота = 1 + max(левая, правая), диаметр через узел = левая + правая. Обновляем глобальный максимум.
2. **Логика:** Рекурсивно или со стеком: post-order. Для каждого узла считаем высоты детей. `diameter = max(diameter, left_h + right_h)`. Возвращаем `1 + max(left_h, right_h)`.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек.

**Ключевой момент:** Диаметр через узел = сумма высот левого и правого поддеревьев. Не обязательно через корень.
