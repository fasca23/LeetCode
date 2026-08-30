---
id: valid-perfect-square
title: 367. Валидный полный квадрат
difficulty: Easy
leetcode_url: https://leetcode.com/problems/valid-perfect-square/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/367_Valid_Perfect_Square
description: Дано положительное число num. Определить, является ли оно полным квадратом (существует целое x: x² = num). Бинарный поиск в [1, num].
screenshots: 0
---

**Подход: Бинарный поиск**

1. **Идея:** Ищем x в диапазоне [1, num] такое что x² = num. На каждом шаге сравниваем mid² с num и сужаем диапазон.
2. **Логика:** `left=1, right=num`. Пока left <= right: `mid=(left+right)//2`. Если `mid*mid == num` → True. Если `< num` → left=mid+1. Иначе right=mid-1.
3. **Время:** O(log n) — бинарный поиск.
4. **Память:** O(1).

**Ключевой момент:** Проверка `mid * mid == num` может переполниться в языках с фиксированным int. В Python не проблема.
