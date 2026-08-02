---
id: contains-duplicate
title: 217. Содержит дубликаты
difficulty: Easy
leetcode_url: https://leetcode.com/problems/contains-duplicate/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/217_Contains_Duplicate
description: Дан массив чисел. Проверить, есть ли в нём дубликаты (хотя бы одно значение встречается дважды). Set: добавляем элементы, если уже есть — дубликат.
screenshots: 0
---

**Подход: Set (хэш-множество)**

1. **Идея:** Проходим по массиву, добавляем элементы в set. Если элемент уже в set — дубликат найден. Set даёт O(1) проверку наличия.
2. **Логика:** `seen = set()`. Для каждого num: если `num in seen` → True. Иначе `seen.add(num)`. После цикла → False.
3. **Время:** O(n) — один проход.
4. **Память:** O(n) — в худшем случае все элементы уникальны.

**Ключевой момент:** Альтернатива — сортировка O(n log n) с O(1) памяти. Set быстрее но требует память.
