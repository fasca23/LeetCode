---
id: construct-string-from-binary-tree
title: 606. Построить строку из бинарного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/construct-string-from-binary-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/606_Construct_String_from_Binary_Tree
description: Дано бинарное дерево. Построить строку с скобками: узел(левый)(правый). Если правый есть а левого нет — нужны пустые скобки (). Рекурсия.
screenshots: 0
---

**Подход: Рекурсия с правилами скобок**

1. **Идея:** Формат: `val(left)(right)`. Правила: если есть левый — всегда скобки. Если есть правый — нужны скобки даже без левого (пустые). Лист — без скобок.
2. **Логика:** `if not node: return ""`. `s = str(node.val)`. Если `node.left`: `s += "(" + recurse(left) + ")"`. Если `node.right`: `s += "(" + recurse(right) + ")"`. Если только правый без левого: `s += "()" + "(" + recurse(right) + ")"`.
3. **Время:** O(n) — каждый узел один раз.
4. **Память:** O(h) — стек рекурсии.

**Ключевой момент:** Если правый ребёнок есть, а левого нет — нужны пустые скобки `()` чтобы указать отсутствие левого.
