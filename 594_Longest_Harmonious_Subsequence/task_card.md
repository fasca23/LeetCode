---
id: longest-harmonious-subsequence
title: 594. Самая длинная гармоничная подпоследовательность
difficulty: Easy
leetcode_url: https://leetcode.com/problems/longest-harmonious-subsequence/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/594_Longest_Harmonious_Subsequence
description: Дан массив. Гармоничная подпоследовательность — разница между max и min ровно 1. Найти максимальную длину. Счётчик частот + проверка пар (x, x+1).
screenshots: 0
---

**Подход: Счётчик частот**

1. **Идея:** Гармоничная = только два значения с разницей 1. Считаем частоты. Для каждого x проверяем пару (x, x+1): `count[x] + count[x+1]`. Берём максимум.
2. **Логика:** `count = Counter(nums)`. `max_len = 0`. Для x в count: если `x+1` в count → `max_len = max(max_len, count[x] + count[x+1])`.
3. **Время:** O(n) — построение счётчика и проход.
4. **Память:** O(n) — счётчик.

**Ключевой момент:** Гармоничная подпоследовательность содержит максимум 2 разных значения (x и x+1). Ищем пару с максимальной суммой частот.
