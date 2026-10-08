---
id: reverse-words-in-a-string-iii
title: 557. Обратные слова в строке III
difficulty: Easy
leetcode_url: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/557_Reverse_Words_in_a_String_III
description: Дана строка. Развернуть каждое слово, сохранив порядок слов и пробелы. Разбиваем по пробелам, разворачиваем каждое слово, склеиваем обратно.
screenshots: 0
---

**Подход: Разбить → развернуть → склеить**

1. **Идея:** Разбиваем строку на слова, каждое разворачиваем, склеиваем через пробел.
2. **Логика:** `words = s.split(' ')`. `reversed_words = [w[::-1] for w in words]`. `return ' '.join(reversed_words)`.
3. **Время:** O(n) — один проход по всем символам.
4. **Память:** O(n) — список слов.

**Ключевой момент:** `w[::-1]` — срез с шагом -1, разворачивает строку. Порядок слов сохраняется.
