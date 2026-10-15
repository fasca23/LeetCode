---
id: shortest-unsorted-continuous-subarray
title: 581. Кратчайший несортированный непрерывный подмассив
difficulty: Medium
leetcode_url: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/581_Shortest_Unsorted_Continuous_Subarray
description: Дан массив. Найти длину кратчайшего подмассива, отсортировав который весь массив станет отсортированным. Копия + сортировка: сравниваем с оригиналом.
screenshots: 0
---

**Подход: Копия + сортировка**

1. **Идея:** Копируем массив, сортируем. Сравниваем с оригиналом: находим первый и последний индексы где они отличаются. Разница + 1 = длина.
2. **Логика:** `sorted_nums = sorted(nums)`. `left = 0, right = n-1`. Двигаем left пока `nums[left] == sorted_nums[left]`. Двигаем right пока `nums[right] == sorted_nums[right]`. Ответ = `max(0, right - left + 1)`.
3. **Время:** O(n log n) — сортировка.
4. **Память:** O(n) — копия.

**Ключевой момент:** Если массив уже отсортирован — left > right → ответ 0.
