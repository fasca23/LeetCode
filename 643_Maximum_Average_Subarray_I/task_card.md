---
id: maximum-average-subarray-i
title: 643. Максимальное среднее подмассива I
difficulty: Easy
leetcode_url: https://leetcode.com/problems/maximum-average-subarray-i/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/643_Maximum_Average_Subarray_I
description: Дан массив и k. Найти максимальное среднее подмассива длины k. Скользящее окно: считаем сумму первого окна, потом сдвигаем — вычитаем левый, добавляем правый.
screenshots: 0
---

**Подход: Скользящее окно**

1. **Идея:** Фиксированная длина k. Считаем сумму первого окна. Сдвигаем: вычитаем ушедший элемент, добавляем новый. Отслеживаем максимум.
2. **Логика:** `window_sum = sum(nums[:k])`, `max_sum = window_sum`. Для i от k до n: `window_sum += nums[i] - nums[i-k]`, `max_sum = max(max_sum, window_sum)`. Вернуть `max_sum / k`.
3. **Время:** O(n) — один проход.
4. **Память:** O(1).

**Ключевой момент:** Скользящее окно даёт O(n) вместо O(n×k) при пересчёте суммы каждый раз.
