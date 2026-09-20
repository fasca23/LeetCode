---
id: number-complement
title: 476. Дополнение числа
difficulty: Easy
leetcode_url: https://leetcode.com/problems/number-complement/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/476_Number_Complement
description: Дано число. Вернуть его дополнение: все биты инвертированы (0→1, 1→0) в пределах значащих битов. Маска = 2^bits - 1, результат = num ^ mask.
screenshots: 0
---

**Подход: XOR с маской из единиц**

1. **Идея:** Дополнение = инвертировать все значащие биты. Строим маску из всех 1 той же длины что и num. XOR с маской инвертирует биты.
2. **Логика:** Считаем биты: `bits = num.bit_length()`. Маска: `mask = (1 << bits) - 1`. Результат: `num ^ mask`.
3. **Время:** O(1) — операции над битами.
4. **Память:** O(1).

**Ключевой момент:** `1 << bits` — это 2^bits. Минус 1 даёт bits единиц: например bits=5 → 11111.
