---
id: perfect-number
title: 507. Совершенное число
difficulty: Easy
leetcode_url: https://leetcode.com/problems/perfect-number/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/507_Perfect_Number
description: Дано число. Совершенное — сумма всех делителей (кроме самого числа) равна числу. 28 = 1+2+4+7+14. Ищем делители до √num.
screenshots: 0
---

**Подход: Перебор делителей до √num**

1. **Идея:** Ищем делители парами: если d делитель, то и num/d делитель. Достаточно перебрать до √num.
2. **Логика:** `if num <= 1: return False`. `total = 1`. Для i от 2 до √num: если num % i == 0 → `total += i`, если i != num/i → `total += num // i`. Вернуть `total == num`.
3. **Время:** O(√n) — перебор до корня.
4. **Память:** O(1).

**Ключевой момент:** Пары делителей (i, num/i). Проверяем `i != num/i` чтобы не добавить квадратный корень дважды.
