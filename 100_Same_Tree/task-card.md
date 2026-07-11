---
id: same-tree
title: 100. Одинаковые деревья
difficulty: Easy
leetcode_url: https://leetcode.com/problems/same-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/100_Same_Tree
description: Даны два бинарных дерева. Проверить, идентичны ли они (структура и значения). Рекурсивное сравнение: оба узла равны, левые равны, правые равны.
screenshots: 0
---
**Подход: Рекурсивный обход**
1. **Идея:** Два дерева одинаковы если: оба пустые → true, одно пустое → false, значения равны и левые поддеревья равны и правые поддеревья равны.
2. **Логика:** `if not p and not q: return True`. `if not p or not q: return False`. `return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)`.
3. **Время:** O(n) — каждый узел проверяется один раз.
4. **Память:** O(h) — стек рекурсии, h высота дерева.
**Ключевой момент:** Проверка на оба None должна быть первой, иначе сломается на `p.val` когда `p is None`.
