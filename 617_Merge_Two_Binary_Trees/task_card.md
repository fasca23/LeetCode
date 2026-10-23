---
id: merge-two-binary-trees
title: 617. Слияние двух бинарных деревьев
difficulty: Easy
leetcode_url: https://leetcode.com/problems/merge-two-binary-trees/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/617_Merge_Two_Binary_Trees
description: Даны два бинарных дерева. Слить: значения перекрывающихся узлов сложить, остальные оставить. Рекурсия: если один None — вернуть другой, иначе сложить и рекурсивно слить детей.
screenshots: 0
---

**Подход: Рекурсивное слияние**

1. **Идея:** Если один узел None — вернуть другой. Если оба есть — сложить значения, рекурсивно слить левых и правых детей.
2. **Логика:** `if not root1: return root2`. `if not root2: return root1`. `root1.val += root2.val`. `root1.left = merge(root1.left, root2.left)`. `root1.right = merge(root1.right, root2.right)`. Вернуть root1.
3. **Время:** O(n + m) — каждый узел обоих деревьев.
4. **Память:** O(h) — стек рекурсии.

**Ключевой момент:** Модифицируем root1 на месте — не создаём новое дерево. Если один None — просто возвращаем другой без изменений.
