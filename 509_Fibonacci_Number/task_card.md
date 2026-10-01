---
id: fibonacci-number
title: 509. Число Фибоначчи
difficulty: Easy
leetcode_url: https://leetcode.com/problems/fibonacci-number/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/509_Fibonacci_Number
description: Дано n. Вернуть n-е число Фибоначчи. F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2). Итеративно с двумя переменными — O(n) времени, O(1) памяти.
screenshots: 0
---

**Подход: Итерация с двумя переменными**

1. **Идея:** Храним только два предыдущих значения. На каждом шаге новое = сумма двух.
2. **Логика:** `if n <= 1: return n`. `prev2, prev1 = 0, 1`. Для i от 2 до n: `cur = prev1 + prev2`, `prev2 = prev1`, `prev1 = cur`. Вернуть prev1.
3. **Время:** O(n) — один проход.
4. **Память:** O(1) — две переменные.

**Ключевой момент:** Не нужен массив — храним только два последних числа. Экономия памяти с O(n) до O(1).
