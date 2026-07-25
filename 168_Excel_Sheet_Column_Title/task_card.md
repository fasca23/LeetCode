---
id: excel-sheet-column-title
title: 168. Заголовок столбца Excel
difficulty: Easy
leetcode_url: https://leetcode.com/problems/excel-sheet-column-title/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/168_Excel_Sheet_Column_Title
description: Дано целое число. Вернуть заголовок столбца Excel (1→A, 28→AB, 701→ZY). Перевод в 26-ричную систему с поправкой: A=1 (не 0), поэтому вычитаем 1 перед % 26.
screenshots: 0
---

**Подход: Перевод в 26-ричную систему**

1. **Идея:** Это как перевод в 26-ричную систему, но цифры 1–26 (A–Z), а не 0–25. Поэтому на каждом шаге вычитаем 1 перед взятием остатка.
2. **Логика:** `while n > 0: n -= 1`, `result = chr(ord('A') + n % 26) + result`, `n //= 26`.
3. **Время:** O(log₂₆ n) — число цифр в 26-ричной записи.
4. **Память:** O(1) — только строка результата.

**Ключевой момент:** `n -= 1` перед `% 26` нужно потому что A=1, а не 0. Без этого 26 даст AZ вместо Z.
