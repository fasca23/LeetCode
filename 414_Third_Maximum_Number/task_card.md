---
id: third-maximum-number
title: 414. Третье максимальное число
difficulty: Easy
leetcode_url: https://leetcode.com/problems/third-maximum-number/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/414_Third_Maximum_Number
description: Дан массив. Найти третье максимальное уникальное число. Если его нет — вернуть максимальное. Set для уникальности, сортировка по убыванию.
screenshots: 0
---

**Подход: Set + сортировка**

1. **Идея:** Убираем дубликаты через set. Если уникальных меньше 3 — возвращаем максимум. Иначе сортируем по убыванию и берём третий.
2. **Логика:** `unique = sorted(set(nums), reverse=True)`. Если `len(unique) < 3` → `unique[0]`. Иначе `unique[2]`.
3. **Время:** O(n log n) — сортировка.
4. **Память:** O(n) — set.

**Ключевой момент:** Уникальность важна. [2,2,3,1] → уникальные [3,2,1] → третье = 1. Без set было бы 2.
