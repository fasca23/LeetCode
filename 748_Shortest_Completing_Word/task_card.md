---
id: shortest-completing-word
title: 748. Кратчайшее дополняющее слово
difficulty: Easy
leetcode_url: https://leetcode.com/problems/shortest-completing-word/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/748_Shortest_Completing_Word
description: Дана строка licensePlate и массив words. Найти кратчайшее слово, содержащее все буквы из licensePlate (без учёта регистра и не-букв). Счётчик частот.
screenshots: 0
---

**Подход: Счётчик + фильтрация**

1. **Идея:** Считаем частоты букв из licensePlate (только буквы, lowercase). Для каждого слова проверяем: содержит ли все нужные буквы в нужном количестве. Выбираем кратчайшее.
2. **Логика:** `need = Counter(ch.lower() for ch in plate if ch.isalpha())`. Для word в words: `have = Counter(word)`. Если `all(have[c] >= need[c] for c in need)` → кандидат. Выбираем min по длине.
3. **Время:** O(n × m) — n слов, m букв.
4. **Память:** O(1) — счётчики алфавита.

**Ключевой момент:** Из licensePlate берём только буквы. Сравниваем частоты: слово должно содержать каждую нужную букву не меньше раз.
