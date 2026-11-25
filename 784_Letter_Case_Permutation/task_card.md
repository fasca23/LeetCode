---
id: letter-case-permutation
title: 784. Перестановка регистра букв
difficulty: Easy
leetcode_url: https://leetcode.com/problems/letter-case-permutation/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/784_Letter_Case_Permutation
description: Дана строка. Вернуть все возможные строки с изменённым регистром букв (цифры не меняются). Бэктрекинг: каждая буква даёт 2 варианта.
screenshots: 0
---

**Подход: Бэктрекинг**

1. **Идея:** Для каждой буквы два варианта: нижний и верхний регистр. Цифры — один вариант. Рекурсивно перебираем все комбинации.
2. **Логика:** `backtrack(i, path)`. Если `i == len(s)` → добавить path. Если цифра → один рекурсивный вызов. Если буква → два: `lower` и `upper`.
3. **Время:** O(2^k × n) — k букв, 2^k комбинаций.
4. **Память:** O(n) — глубина рекурсии.

**Ключевой момент:** Цифры не дают развилки — только один путь. Буквы дают два (lower/upper).
