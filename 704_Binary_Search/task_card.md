---
id: binary-search
title: 704. Бинарный поиск
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-search/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/704_Binary_Search
description: Дан отсортированный массив и target. Найти индекс target или -1. Классический бинарный поиск: mid, сравнение, сужение диапазона вдвое.
screenshots: 0
---

**Подход: Классический бинарный поиск**

1. **Идея:** Берём середину диапазона. Если равно target — нашли. Если target больше — ищем справа. Меньше — слева. Диапазон сужается вдвое.
2. **Логика:** `left=0, right=n-1`. Пока left <= right: `mid=(left+right)//2`. Если `nums[mid] == target` → mid. Если `< target` → `left=mid+1`. Иначе `right=mid-1`. Вернуть -1.
3. **Время:** O(log n) — диапазон сужается вдвое.
4. **Память:** O(1).

**Ключевой момент:** `while left <= right` (не `<`). `right = mid - 1`, `left = mid + 1` — mid уже проверен.
