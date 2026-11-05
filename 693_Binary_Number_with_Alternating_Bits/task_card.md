---
id: binary-number-with-alternating-bits
title: 693. Бинарное число с чередующимися битами
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-number-with-alternating-bits/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/693_Binary_Number_with_Alternating_Bits
description: Дано число n. Проверить, чередуются ли биты в его двоичном представлении (101, 1010). Трюк: n ^ (n >> 1) даёт все единицы если биты чередуются. Проверка n & (n+1) == 0.
screenshots: 0
---

**Подход: XOR со сдвигом**

1. **Идея:** Если биты чередуются (101010), то `n ^ (n >> 1)` даёт все единицы (111111). Число из всех единиц: `n & (n+1) == 0`.
2. **Логика:** `x = n ^ (n >> 1)`. Вернуть `(x & (x + 1)) == 0`.
3. **Время:** O(1) — одна операция.
4. **Память:** O(1).

**Ключевой момент:** `n ^ (n >> 1)` сдвигает и XOR'ит: соседние биты сравниваются. Если чередуются — все различия = 1, результат = все единицы.
