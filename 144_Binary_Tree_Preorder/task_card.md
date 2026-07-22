---
id: binary-tree-preorder-traversal
title: 144. Preorder-обход бинарного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/144_Binary_Tree_Preorder
description: Дан корень бинарного дерева. Вернуть значения в preorder-обходе (корень → левый → правый). Итеративно со стеком: push правого, затем левого — левый выйдет первым.
screenshots: 0
---

**Подход: Итеративный обход со стеком**

1. **Идея:** Preorder = корень, потом левое, потом правое. Стек LIFO: чтобы левый вышел первым, кладём его последним (после правого).
2. **Логика:** `stack = [root]`. Пока стек: `node = stack.pop()`, добавить в результат. Если `node.right` → push. Если `node.left` → push.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек в куче, высота дерева.

**Ключевой момент:** Порядок push: сначала правый, потом левый. pop() достанет левый первым → обход корень-лево-право.
