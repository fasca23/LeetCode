---
id: longest-uncommon-subsequence-i
title: 521. Самая длинная необычная подпоследовательность I
difficulty: Easy
leetcode_url: https://leetcode.com/problems/longest-uncommon-subsequence-i/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/521_Longest_Uncommon_Subsequence_I
description: Даны две строки a и b. Найти длину самой длинной необычной подпоследовательности (есть только у одной из строк). Если строки разные — ответ max(len(a), len(b)), иначе -1.
screenshots: 0
---

**Подход: Математическое наблюдение**

1. **Идея:** Если строки разные — сама большая строка является необычной подпоследовательностью (её нет у другой). Ответ = max(len(a), len(b)). Если строки равны — необычной нет.
2. **Логика:** `if a == b: return -1`. `return max(len(a), len(b))`.
3. **Время:** O(1) — сравнение строк O(min(n,m)).
4. **Память:** O(1).

**Ключевой момент:** Если строки разные, вся большая строка — необычная подпоследовательность для меньшей. Не нужно ничего искать.
