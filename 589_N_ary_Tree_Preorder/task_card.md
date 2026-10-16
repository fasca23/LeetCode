---
id: n-ary-tree-preorder-traversal
title: 589. Preorder-обход N-арного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/589_N_ary_Tree_Preorder
description: Дано N-арное дерево. Вернуть preorder-обход (корень → дети слева направо). Стек: push детей в обратном порядке чтобы левый вышел первым.
screenshots: 0
---

**Подход: Итеративный стек**

1. **Идея:** Preorder: сначала корень, потом дети. Стек LIFO: чтобы первый ребёнок вышел первым — push детей в обратном порядке.
2. **Логика:** `stack = [root]`. Пока стек: `node = stack.pop()`, добавить в результат. Для children в обратном порядке: push в стек.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек в куче.

**Ключевой момент:** `reversed(node.children)` — чтобы первый ребёнок оказался наверху стека.
