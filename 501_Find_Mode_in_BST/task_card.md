---
id: find-mode-in-binary-search-tree
title: 501. Поиск моды в бинарном дереве поиска
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/501_Find_Mode_in_BST
description: Дано BST. Найти моду (наиболее часто встречающееся значение). Inorder-обход даёт отсортированный порядок, считаем подряд идущие одинаковые.
screenshots: 0
---

**Подход: Inorder-обход (отсортированный порядок)**

1. **Идея:** В BST inorder даёт отсортированный список. Одинаковые значения идут подряд. Считаем серии и находим максимальную.
2. **Логика:** Inorder обход со стеком. Для каждого узла: если значение = предыдущему → `count += 1`. Иначе `count = 1`. Обновляем `max_count` и список мод.
3. **Время:** O(n) — один обход.
4. **Память:** O(h) — стек.

**Ключевой момент:** В BST одинаковые значения всегда идут подряд при inorder. Не нужен словарь частот.
