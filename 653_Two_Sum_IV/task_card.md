---
id: two-sum-iv-input-is-a-bst
title: 653. Сумма двух IV — вход BST
difficulty: Easy
leetcode_url: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/653_Two_Sum_IV
description: Дано BST и цель k. Проверить, есть ли два узла с суммой k. Inorder-обход даёт отсортированный массив, затем два указателя как в 1. Two Sum.
screenshots: 0
---

**Подход: Inorder + два указателя**

1. **Идея:** Inorder BST даёт отсортированный список. В отсортированном массиве ищем пару с суммой k двумя указателями.
2. **Логика:** Inorder обход со стеком → `values`. `left=0, right=len-1`. Пока left < right: `s = values[left] + values[right]`. Если s == k → True. Если s < k → left++. Иначе right--.
3. **Время:** O(n) — inorder + два указателя.
4. **Память:** O(n) — массив значений.

**Ключевой момент:** BST + inorder = отсортированный массив. Дальше задача сводится к Two Sum на отсортированном массиве.
