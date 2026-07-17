---
id: balanced-binary-tree
title: 110. Сбалансированное бинарное дерево
difficulty: Easy
leetcode_url: https://leetcode.com/problems/balanced-binary-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/110_Balanced_Binary_Tree
description: Дано бинарное дерево. Проверить, сбалансировано ли оно (разница высот ≤ 1 для всех узлов). Post-order DFS: высоты снизу вверх, флаг -1 при дисбалансе.
screenshots: 0
---

**Подход: Post-order DFS со стеком**

1. **Идея:** Обходим дерево снизу вверх. Каждый узел возвращает высоту своего поддерева. Если разница высот левого и правого > 1 — дерево не сбалансировано.
2. **Логика:** Стек хранит `(узел, visited)`. Первый раз — кладём детей. Второй раз — дети обработаны, вычисляем: `left_h = heights[node.left]`, `right_h = heights[node.right]`. Если `abs(left_h - right_h) > 1` → False. Иначе `heights[node] = 1 + max(left_h, right_h)`.
3. **Почему post-order:** Нужно знать высоты детей ДО того как вычислим высоту родителя. Post-order (снизу вверх) даёт именно это.
4. **Время:** O(n) — каждый узел дважды (push + pop).
5. **Память:** O(h) — стек + словарь высот. Стек в куче, не упадёт.

**Ключевой момент:** Флаг `visited` в стеке позволяет имитировать post-order без рекурсии: первый раз кладём детей, второй раз — обрабатываем узел.
