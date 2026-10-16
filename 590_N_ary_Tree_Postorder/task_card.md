---
id: n-ary-tree-postorder-traversal
title: 590. Postorder-обход N-арного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/590_N_ary_Tree_Postorder
description: Дано N-арное дерево. Вернуть postorder-обход (дети слева направо, потом корень). Стек с visited-флагом или трюк с reverse.
screenshots: 0
---

**Подход: Трюк с reverse (preorder + reverse)**

1. **Идея:** Postorder = reverse(модифицированный preorder). Если в preorder пушить детей в прямом порядке и добавлять в результат, получим корень→дети справа налево. Reverse результата = postorder.
2. **Логика:** `stack = [root]`, `result = []`. Пока стек: `node = stack.pop()`, `result.append(node.val)`. Push детей в ПРЯМОМ порядке. В конце `return result[::-1]`.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек.

**Ключевой момент:** Push детей в прямом порядке + reverse результата = postorder. Без visited-флага.
