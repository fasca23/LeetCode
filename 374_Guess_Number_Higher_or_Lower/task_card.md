---
id: guess-number-higher-or-lower
title: 374. Угадай число (выше или ниже)
difficulty: Easy
leetcode_url: https://leetcode.com/problems/guess-number-higher-or-lower/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/374_Guess_Number_Higher_or_Lower
description: Дано число n. Угадать загаданное число используя API guess(num): -1 если загаданное меньше, 1 если больше, 0 если угадали. Бинарный поиск в [1, n].
screenshots: 0
---

**Подход: Бинарный поиск**

1. **Идея:** Классический бинарный поиск. Берём середину диапазона, спрашиваем guess(mid). Ответ -1 → ищем левее, 1 → правее, 0 → нашли.
2. **Логика:** `left=1, right=n`. Пока left <= right: `mid=(left+right)//2`. `res = guess(mid)`. Если 0 → mid. Если -1 → right=mid-1. Если 1 → left=mid+1.
3. **Время:** O(log n) — бинарный поиск.
4. **Память:** O(1).

**Ключевой момент:** guess(mid) говорит куда двигаться. Это как бинарный поиск но вместо сравнения с target — вызов API.
