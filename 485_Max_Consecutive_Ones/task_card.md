---
id: max-consecutive-ones
title: 485. Максимум подряд идущих единиц
difficulty: Easy
leetcode_url: https://leetcode.com/problems/max-consecutive-ones/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/485_Max_Consecutive_Ones
description: Дан бинарный массив. Найти максимальное количество подряд идущих единиц. Один проход: счётчик текущей серии, обновляем максимум.
screenshots: 0
---

**Подход: Один проход со счётчиком**

1. **Идея:** Идём по массиву. Встретили 1 — увеличиваем счётчик. Встретили 0 — сбрасываем. На каждом шаге обновляем максимум.
2. **Логика:** `count = max_count = 0`. Для num в nums: если `num == 1` → `count += 1`, `max_count = max(max_count, count)`. Иначе `count = 0`.
3. **Время:** O(n) — один проход.
4. **Память:** O(1).

**Ключевой момент:** Счётчик сбрасывается на 0 при встрече нуля. Максимум обновляется только при единице.
