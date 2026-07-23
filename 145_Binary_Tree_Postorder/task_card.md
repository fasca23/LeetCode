---
id: binary-tree-postorder-traversal
title: 145. Postorder-обход бинарного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/145_Binary_Tree_Postorder
description: Дан корень бинарного дерева. Вернуть значения в postorder-обходе (левый → правый → корень). Итеративно с visited-флагом: первый раз кладём детей, второй — добавляем в результат.
screenshots: 0
---

**Подход: Итеративный обход с visited-флагом**

1. **Идея:** Postorder = левое, правое, корень. В стеке храним `(узел, visited)`. Первый раз (False) — кладём обратно с True и добавляем детей. Второй раз (True) — дети обработаны, добавляем в результат.
2. **Логика:** `stack = [(root, False)]`. Пока стек: `node, visited = stack.pop()`. Если visited → `result.append(node.val)`. Иначе: `stack.append((node, True))`, push правого, push левого.
3. **Время:** O(n) — каждый узел дважды в стеке.
4. **Память:** O(h) — стек в куче.

**Ключевой момент:** Порядок push детей: сначала правый, потом левый. Левый выйдет первым и обработается раньше. Родитель с visited=True выходит после обоих детей.
