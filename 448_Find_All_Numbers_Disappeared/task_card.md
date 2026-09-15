---
id: find-all-numbers-disappeared-in-an-array
title: 448. Найти все пропавшие числа в массиве
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/448_Find_All_Numbers_Disappeared
description: Дан массив из n чисел в диапазоне [1, n]. Некоторые числа повторяются, некоторые отсутствуют. Найти все отсутствующие. Помечаем индексы отрицательными.
screenshots: 0
---

**Подход: Пометка индексов**

1. **Идея:** Число x встречается → помечаем индекс x-1 отрицательным. Второй проход: если nums[i] > 0, значит число i+1 отсутствует.
2. **Логика:** Первый проход: для каждого num → `idx = abs(num) - 1`, `nums[idx] = -abs(nums[idx])`. Второй проход: если `nums[i] > 0` → `i+1` отсутствует.
3. **Время:** O(n) — два прохода.
4. **Память:** O(1) — не считая результата.

**Ключевой момент:** Используем сам массив как маркер. Знак минус = "это число встречалось". Никакой доп. памяти.
