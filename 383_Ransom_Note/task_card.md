---
id: ransom-note
title: 383. Записка с выкупом
difficulty: Easy
leetcode_url: https://leetcode.com/problems/ransom-note/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/383_Ransom_Note
description: Даны две строки: ransomNote и magazine. Проверить, можно ли составить ransomNote из букв magazine (каждую букву использовать один раз). Счётчик частот.
screenshots: 0
---

**Подход: Счётчик частот**

1. **Идея:** Считаем частоты букв в magazine. Для каждой буквы ransomNote уменьшаем счётчик. Если буквы нет или счётчик < 0 — невозможно.
2. **Логика:** `count = Counter(magazine)`. Для ch в ransomNote: если `count[ch] == 0` → False. Иначе `count[ch] -= 1`.
3. **Время:** O(n + m) — проход по обеим строкам.
4. **Память:** O(1) — алфавит ограничен (26 букв).

**Ключевой момент:** Каждая буква magazine может быть использована только один раз. Счётчик это гарантирует.
