---
id: container-with-most-water
title: 11. Контейнер с наибольшим количеством воды
difficulty: Medium
leetcode_url: https://leetcode.com/problems/container-with-most-water/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/11_Container_With_Most_Water
description: Дан массив высот. Найти две линии, которые вместе с осью X образуют контейнер с максимальным объёмом воды. Два указателя: слева и справа, двигаем меньшую высоту.
screenshots: 0
---

**Подход: Два указателя**

1. **Идея:** Указатели left и right на краях. Площадь = min(height[left], height[right]) × (right - left). Двигаем тот указатель, где высота меньше (большая высота не поможет — площадь ограничена меньшей).
2. **Логика:** `left=0, right=n-1, max_area=0`. Пока left < right: `area = min(h[left], h[right]) * (right - left)`, обновить max. Если `h[left] < h[right]` → left++, иначе right--.
3. **Время:** O(n) — один проход.
4. **Память:** O(1) — две переменные.

**Ключевой момент:** Площадь ограничена меньшей высотой. Двигать большую бессмысленно — ширина уменьшится, а высота не вырастет.
