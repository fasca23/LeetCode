---
id: rotate-string
title: 796. Поворот строки
difficulty: Easy
leetcode_url: https://leetcode.com/problems/rotate-string/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/796_Rotate_String
description: Даны строки s и goal. Проверить, можно ли получить goal из s циклическим сдвигом. Трюк: goal в (s + s) если длины равны.
screenshots: 0
---

**Подход: Удвоение строки**

1. **Идея:** Циклический сдвиг s — это подстрока в s + s. Если goal можно получить сдвигом, он найдётся в s + s.
2. **Логика:** `if len(s) != len(goal): return False`. `return goal in (s + s)`.
3. **Время:** O(n) — поиск подстроки.
4. **Память:** O(n) — удвоенная строка.

**Ключевой момент:** Сначала проверяем длины. Потом ищем goal в удвоенной s.
