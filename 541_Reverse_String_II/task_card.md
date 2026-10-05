---
id: reverse-string-ii
title: 541. Обратная строка II
difficulty: Easy
leetcode_url: https://leetcode.com/problems/reverse-string-ii/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/541_Reverse_String_II
description: Дана строка s и число k. Каждые 2k символов: развернуть первые k, оставить вторые k как есть. Шагаем по 2k, разворачиваем первые k в блоке.
screenshots: 0
---

**Подход: Шаг по 2k + разворот первых k**

1. **Идея:** Идём блоками по 2k. В каждом блоке разворачиваем первые k символов (или меньше, если блок короче). Остальное не трогаем.
2. **Логика:** `chars = list(s)`. Для i от 0 до n с шагом 2k: `left = i`, `right = min(i + k - 1, n - 1)`. Разворачиваем chars[left..right].
3. **Время:** O(n) — один проход.
4. **Память:** O(n) — список символов.

**Ключевой момент:** `right = min(i + k - 1, n - 1)` — если символов меньше k, разворачиваем только доступные.
