---
id: maximum-product-of-three-numbers
title: 628. Максимальное произведение трёх чисел
difficulty: Easy
leetcode_url: https://leetcode.com/problems/maximum-product-of-three-numbers/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/628_Maximum_Product_of_Three_Numbers
description: Дан массив. Найти максимальное произведение трёх чисел. Сортируем: либо три наибольших, либо два наименьших (отрицательных) и наибольшее.
screenshots: 0
---

**Подход: Сортировка + два варианта**

1. **Идея:** Максимум либо из трёх наибольших, либо из двух наименьших (отрицательных) и наибольшего. Оба варианта проверяем.
2. **Логика:** `nums.sort()`. `case1 = nums[-1] * nums[-2] * nums[-3]`. `case2 = nums[0] * nums[1] * nums[-1]`. Вернуть `max(case1, case2)`.
3. **Время:** O(n log n) — сортировка.
4. **Память:** O(1).

**Ключевой момент:** Два отрицательных числа дают положительное произведение. Если в массиве есть большие отрицательные — их произведение с максимумом может быть больше.
