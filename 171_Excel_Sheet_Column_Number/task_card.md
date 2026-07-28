---
id: excel-sheet-column-number
title: 171. Номер столбца Excel
difficulty: Easy
leetcode_url: https://leetcode.com/problems/excel-sheet-column-number/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/171_Excel_Sheet_Column_Number
description: Дана строка — заголовок столбца Excel (A, AB, ZY). Вернуть номер столбца (A→1, AB→28, ZY→701). Перевод из 26-ричной системы: каждая буква = цифра 1–26.
screenshots: 0
---

**Подход: Перевод из 26-ричной системы**

1. **Идея:** Каждая буква A–Z = число 1–26. Идём слева направо: `result = result * 26 + value`. Это как перевод из системы счисления с основанием 26.
2. **Логика:** `result = 0`. Для каждой буквы: `value = ord(ch) - ord('A') + 1`, `result = result * 26 + value`.
3. **Время:** O(n) — один проход по строке.
4. **Память:** O(1) — одна переменная.

**Ключевой момент:** Это обратная задача к 168. Здесь из букв в число, там из числа в буквы.
