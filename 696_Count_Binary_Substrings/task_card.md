---
id: count-binary-substrings
title: 696. Подсчёт бинарных подстрок
difficulty: Easy
leetcode_url: https://leetcode.com/problems/count-binary-substrings/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/696_Count_Binary_Substrings
description: Дана бинарная строка. Посчитать подстроки с равным числом 0 и 1 подряд (0011, 01, 1100). Группируем подряд идущие одинаковые символы, сумма min(prev, curr) для соседних групп.
screenshots: 0
---

**Подход: Группировка + min соседних групп**

1. **Идея:** Группируем подряд идущие символы: "00110011" → [2,2,2,2]. Для каждой пары соседних групп можно составить min(len1, len2) валидных подстрок.
2. **Логика:** `groups = []`. Считаем длину серии, при смене — добавляем. `total = sum(min(groups[i], groups[i+1]) for i in range(len(groups)-1))`.
3. **Время:** O(n) — один проход.
4. **Память:** O(n) — группы.

**Ключевой момент:** Валидная подстрока = две соседние группы одинаковых символов, взятые по min длине.
