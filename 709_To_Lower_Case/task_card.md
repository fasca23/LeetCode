---
id: to-lower-case
title: 709. В нижний регистр
difficulty: Easy
leetcode_url: https://leetcode.com/problems/to-lower-case/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/709_To_Lower_Case
description: Дана строка. Перевести все буквы в нижний регистр. Без встроенного lower(). Проходим посимвольно, если заглавная — заменяем через ord/chr.
screenshots: 0
---

**Подход: Посимвольная замена**

1. **Идея:** Проходим по строке. Если символ — заглавная буква (A-Z), заменяем на строчную. Формула: `chr(ord(ch) + 32)`.
2. **Логика:** `result = []`. Для ch в s: если `'A' <= ch <= 'Z'` → `chr(ord(ch) + 32)`, иначе ch. `return ''.join(result)`.
3. **Время:** O(n) — один проход.
4. **Память:** O(n) — строка результата.

**Ключевой момент:** Разница между 'A' и 'a' в ASCII = 32. `ord('a') - ord('A') = 32`.
