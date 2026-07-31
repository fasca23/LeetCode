---
id: string-to-integer-atoi
title: 8. Преобразование строки в целое число (atoi)
difficulty: Medium
leetcode_url: https://leetcode.com/problems/string-to-integer-atoi/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/8_String_to_Integer_atoi
description: Реализовать функцию atoi: строка → 32-битное целое. Пропустить пробелы, определить знак, считать цифры. При переполнении вернуть INT_MAX или INT_MIN.
screenshots: 0
---

**Подход: Пошаговая обработка строки**

1. **Идея:** Обрабатываем строку по правилам: пробелы → знак → цифры → проверка переполнения. Без встроенных функций конвертации.
2. **Логика:** `i = 0`. Пропустить пробелы. Определить знак (±). Считать цифры: `result = result * 10 + digit`. Проверить переполнение ДО умножения.
3. **Время:** O(n) — один проход по строке.
4. **Память:** O(1) — только переменные.

**Ключевой момент:** Проверка переполнения: `if result > (INT_MAX - digit) // 10` — это гарантирует что `result * 10 + digit` не выйдет за границы.
