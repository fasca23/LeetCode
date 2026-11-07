---
id: degree-of-an-array
title: 697. Степень массива
difficulty: Easy
leetcode_url: https://leetcode.com/problems/degree-of-an-array/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/697_Degree_of_An_Array
description: Дан массив. Степень = максимальная частота элемента. Найти минимальную длину подмассива с той же степенью. Считаем частоты и границы (первый/последний индекс).
screenshots: 0
---

**Подход: Частоты + границы**

1. **Идея:** Степень = max частота. Для элементов с этой частотой ищем минимальную длину = last_index - first_index + 1.
2. **Логика:** Считаем `count`, `first`, `last`. `degree = max(count.values())`. Для x в count: если `count[x] == degree` → `min_len = min(min_len, last[x] - first[x] + 1)`.
3. **Время:** O(n) — три прохода.
4. **Память:** O(n) — три словаря.

**Ключевой момент:** Подмассив со степенью degree должен содержать все вхождения элемента с этой частотой. Минимум — от первого до последнего.
