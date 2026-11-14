---
id: find-pivot-index
title: 724. Найти опорный индекс
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-pivot-index/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/724_Find_Pivot_Index
description: Дан массив. Найти индекс где сумма слева = сумме справа. Префиксные суммы или один проход с total: left_sum == total - left_sum - nums[i].
screenshots: 0
---

**Подход: Один проход с общей суммой**

1. **Идея:** `total = sum(nums)`. Идём по массиву, поддерживаем `left_sum`. Правую сумму можно вычислить: `right_sum = total - left_sum - nums[i]`. Если равны — нашли pivot.
2. **Логика:** `total = sum(nums)`, `left_sum = 0`. Для i, num: `if left_sum == total - left_sum - num: return i`. `left_sum += num`. Вернуть -1.
3. **Время:** O(n) — один проход.
4. **Память:** O(1).

**Ключевой момент:** Не нужно явно считать правую сумму — она выводится из общей и левой. Один проход вместо двух.
