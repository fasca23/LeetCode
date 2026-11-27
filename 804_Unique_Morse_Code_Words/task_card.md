---
id: unique-morse-code-words
title: 804. Уникальные слова азбуки Морзе
difficulty: Easy
leetcode_url: https://leetcode.com/problems/unique-morse-code-words/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/804_Unique_Morse_Code_Words
description: Дан массив слов. Перевести каждое в азбуку Морзе, посчитать количество уникальных кодов. Таблица Морзе + set для уникальности.
screenshots: 0
---

**Подход: Таблица Морзе + set**

1. **Идея:** Для каждого слова строим код Морзе (конкатенация кодов букв). Складываем в set — уникальные.
2. **Логика:** `morse = [".-","-...",...]`. Для word в words: `code = ''.join(morse[ord(ch) - ord('a')] for ch in word)`. `seen.add(code)`. Вернуть `len(seen)`.
3. **Время:** O(n × m) — n слов, m букв.
4. **Память:** O(n) — set кодов.

**Ключевой момент:** Разные слова могут дать одинаковый код Морзе (например "a" и ".-"? нет, но "abc" и другой набор букв могут совпасть). Set убирает дубликаты.
