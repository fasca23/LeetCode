---
id: set-mismatch
title: 645. Несоответствие множества
difficulty: Easy
leetcode_url: https://leetcode.com/problems/set-mismatch/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/645_Set_Mismatch
description: Массив из n чисел от 1 до n. Одно число продублировано, одно отсутствует. Найти оба. Счётчик частот: частота 2 — дубликат, частота 0 — отсутствующее.
screenshots: 0
---

**Подход: Счётчик частот**

1. **Идея:** Считаем частоты всех чисел от 1 до n. Число с частотой 2 — дубликат. Число с частотой 0 — отсутствующее.
2. **Логика:** `count = [0] * (n + 1)`. Для num в nums: `count[num] += 1`. Для i от 1 до n: если `count[i] == 2` → duplicate, если `count[i] == 0` → missing. Вернуть [duplicate, missing].
3. **Время:** O(n) — два прохода.
4. **Память:** O(n) — массив частот.

**Ключевой момент:** Числа от 1 до n — можно использовать массив вместо словаря. Индексы = числа.
