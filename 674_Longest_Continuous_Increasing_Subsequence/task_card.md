---
id: longest-continuous-increasing-subsequence
title: 674. Самая длинная непрерывная возрастающая подпоследовательность
difficulty: Easy
leetcode_url: https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/674_Longest_Continuous_Increasing_Subsequence
description: Дан массив. Найти длину самой длинной непрерывной возрастающей подпоследовательности. Один проход: счётчик текущей серии, обновляем максимум.
screenshots: 0
---

**Подход: Один проход со счётчиком**

1. **Идея:** Идём по массиву. Если текущий > предыдущего — серия растёт. Иначе сбрасываем счётчик. Обновляем максимум.
2. **Логика:** `count = 1`, `max_count = 1`. Для i от 1: если `nums[i] > nums[i-1]` → `count += 1`, `max_count = max(max_count, count)`. Иначе `count = 1`.
3. **Время:** O(n) — один проход.
4. **Память:** O(1).

**Ключевой момент:** Строго возрастающая (не ≥). При равенстве или убывании серия сбрасывается.
