---
id: prime-number-of-set-bits
title: 762. Простое число единичных битов
difficulty: Easy
leetcode_url: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/762_Prime_Number_of_Set_Bits
description: Даны left и right. Посчитать числа в диапазоне, у которых количество единичных битов — простое число. Простые до 32: 2,3,5,7,11,13,17,19,23,29,31.
screenshots: 0
---

**Подход: Подсчёт битов + проверка простоты**

1. **Идея:** Для каждого числа в [left, right] считаем единичные биты. Проверяем, простое ли это число. Максимум битов у 32-битного числа = 32, простые до 32 можно захардкодить.
2. **Логика:** `primes = {2,3,5,7,11,13,17,19,23,29,31}`. Для num в range: `bits = bin(num).count('1')`. Если bits в primes → count++.
3. **Время:** O((right-left) × log right) — для каждого числа считаем биты.
4. **Память:** O(1).

**Ключевой момент:** Простые числа до 32 известны заранее — не нужно проверять простоту. Множество для O(1) проверки.
