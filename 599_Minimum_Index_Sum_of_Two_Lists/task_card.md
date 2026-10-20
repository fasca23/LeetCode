---
id: minimum-index-sum-of-two-lists
title: 599. Минимальная сумма индексов двух списков
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/599_Minimum_Index_Sum_of_Two_Lists
description: Даны два списка ресторанов. Найти общие рестораны с минимальной суммой индексов. Словарь индексов первого списка, для второго считаем сумму.
screenshots: 0
---

**Подход: Словарь индексов + минимум**

1. **Идея:** Запоминаем индексы элементов list1 в словаре. Для каждого элемента list2: если он есть в list1 — считаем сумму индексов. Обновляем минимум и результат.
2. **Логика:** `index1 = {name: i for i, name in enumerate(list1)}`. `min_sum = inf`, `result = []`. Для j, name в enumerate(list2): если name в index1 → `total = index1[name] + j`. Если total < min_sum → обновить, сбросить result. Если == → добавить.
3. **Время:** O(n + m) — два прохода.
4. **Память:** O(n) — словарь.

**Ключевой момент:** Если несколько пар с одинаковой минимальной суммой — вернуть все.
