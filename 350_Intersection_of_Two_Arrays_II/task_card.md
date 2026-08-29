---
id: intersection-of-two-arrays-ii
title: 350. Пересечение двух массивов II
difficulty: Easy
leetcode_url: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/350_Intersection_of_Two_Arrays_II
description: Даны два массива. Вернуть пересечение с учётом кратности (если число встречается 2 раза в обоих — в результате 2 раза). Счётчик частот.
screenshots: 0
---

**Подход: Счётчик частот**

1. **Идея:** В отличие от 349, здесь важна кратность. Считаем частоты в nums1. Для каждого num из nums2: если счётчик > 0 — добавляем в результат и уменьшаем счётчик.
2. **Логика:** `count = Counter(nums1)`. `result = []`. Для num в nums2: если `count[num] > 0` → `result.append(num)`, `count[num] -= 1`.
3. **Время:** O(n + m) — построение счётчика и проход по nums2.
4. **Память:** O(n) — счётчик.

**Ключевой момент:** Уменьшение счётчика гарантирует что элемент не будет добавлен больше раз чем есть в nums1.
