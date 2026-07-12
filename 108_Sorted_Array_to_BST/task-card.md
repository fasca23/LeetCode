---
id: convert-sorted-array-to-bst
title: 108. Массив в бинарное дерево поиска
difficulty: Easy
leetcode_url: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/108_Sorted_Array_to_BST
description: Дан отсортированный массив. Построить сбалансированное BST (высота отличается не более чем на 1). Бинарный выбор середины как корня.
screenshots: 0
---
**Подход: Рекурсивное построение с выбором середины**
1. **Идея:** Чтобы BST был сбалансированным, корень = середина массива. Левое поддерево = левая половина. Правое = правая половина. Повторяем рекурсивно.
2. **Логика:** `mid = (left + right) // 2`. `root = TreeNode(nums[mid])`. `root.left = build(left, mid-1)`. `root.right = build(mid+1, right)`. База: `left > right` → None.
3. **Время:** O(n) — каждый элемент один раз становится узлом.
4. **Память:** O(log n) — стек рекурсии для сбалансированного дерева.
**Ключевой момент:** Выбор середины гарантирует что левое и правое поддеревья отличаются по размеру не более чем на 1.
