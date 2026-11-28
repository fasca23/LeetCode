---
id: number-of-lines-to-write-string
title: 806. Количество строк для записи строки
difficulty: Easy
leetcode_url: https://leetcode.com/problems/number-of-lines-to-write-string/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/806_Number_of_Lines_To_Write_String
description: Даны ширины букв и строка s. Пишем на строках шириной 100. Вернуть [количество строк, ширина последней]. Один проход: если не влезает — новая строка.
screenshots: 0
---

**Подход: Один проход с накоплением ширины**

1. **Идея:** Идём по строке. Добавляем ширину буквы к текущей строке. Если превышает 100 — начинаем новую строку.
2. **Логика:** `lines = 1`, `width = 0`. Для ch в s: `w = widths[ord(ch) - ord('a')]`. Если `width + w > 100`: `lines += 1`, `width = w`. Иначе `width += w`. Вернуть `[lines, width]`.
3. **Время:** O(n) — один проход.
4. **Память:** O(1).

**Ключевой момент:** Буква не переносится частично — если не влезает, начинаем новую строку.
