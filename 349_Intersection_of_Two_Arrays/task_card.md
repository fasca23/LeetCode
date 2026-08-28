---
id: intersection-of-two-arrays
title: 349. Пересечение двух массивов
difficulty: Easy
leetcode_url: https://leetcode.com/problems/intersection-of-two-arrays/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/349_Intersection_of_Two_Arrays
description: Даны два массива. Вернуть массив уникальных элементов, которые есть в обоих. Set: превращаем первый в множество, проверяем элементы второго.
screenshots: 0
---

**Подход: Set (множество)**

1. **Идея:** Множество set1 из nums1. Проходим по nums2: если элемент в set1 — добавляем в результат (тоже set для уникальности).
2. **Логика:** `set1 = set(nums1)`, `result = set()`. Для num в nums2: если num в set1 → `result.add(num)`. Вернуть `list(result)`.
3. **Время:** O(n + m) — построение set1 и проход по nums2.
4. **Память:** O(n) — множество set1.

**Ключевой момент:** Set автоматически убирает дубликаты. Результат — уникальные элементы.
