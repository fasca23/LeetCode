---
id: search-in-a-binary-search-tree
title: 700. Поиск в бинарном дереве поиска
difficulty: Easy
leetcode_url: https://leetcode.com/problems/search-in-a-binary-search-tree/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/700_Search_in_a_BST
description: Дано BST и значение val. Найти узел со значением val и вернуть его поддерево. Если нет — None. Итеративно: val < node.val → влево, val > node.val → вправо.
screenshots: 0
---

**Подход: Итеративный поиск в BST**

1. **Идея:** В BST левые < корень < правые. Сравниваем val с текущим узлом и идём в нужную сторону.
2. **Логика:** `current = root`. Пока current: если `val == current.val` → вернуть current. Если `val < current.val` → `current = current.left`. Иначе → `current = current.right`.
3. **Время:** O(h) — высота дерева. Для сбалансированного O(log n).
4. **Память:** O(1).

**Ключевой момент:** BST свойство позволяет отбрасывать половину дерева на каждом шаге. Не нужен полный обход.
