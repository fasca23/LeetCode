---
id: design-hashmap
title: 706. Реализация HashMap
difficulty: Easy
leetcode_url: https://leetcode.com/problems/design-hashmap/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/706_Design_HashMap
description: Реализовать HashMap без встроенных структур. put, get, remove. Массив корзин, хэш key % size, в корзине список пар (key, value).
screenshots: 0
---

**Подход: Массив корзин + пары ключ-значение**

1. **Идея:** Как HashSet, но храним пары (key, value). put — обновить или добавить. get — найти значение. remove — удалить пару.
2. **Логика:** `buckets = [[] for _ in range(1000)]`. `put(key, value)`: idx = key % 1000, ищем key в списке — обновляем или добавляем. `get`: ищем key, возвращаем value или -1. `remove`: удаляем пару.
3. **Время:** O(1) в среднем, O(n) в худшем.
4. **Память:** O(n) — все пары.

**Ключевой момент:** Отличие от HashSet — храним значение вместе с ключом. В корзине список пар `[key, value]`.
