---
id: relative-ranks
title: 506. Относительные ранги
difficulty: Easy
leetcode_url: https://leetcode.com/problems/relative-ranks/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/506_Relative_Ranks
description: Дан массив очков. Присвоить ранги: 1-е место — "Gold Medal", 2-е — "Silver Medal", 3-е — "Bronze Medal", остальные — номер места. Сортируем с индексами.
screenshots: 0
---

**Подход: Сортировка с индексами**

1. **Идея:** Сортируем пары (очки, индекс) по убыванию очков. Первым трём даём медали, остальным — номер места (4, 5, 6...). Записываем в результат по исходному индексу.
2. **Логика:** `pairs = sorted(enumerate(score), key=lambda x: -x[1])`. Для i, (idx, val) в enumerate(pairs): если i=0 → "Gold Medal", i=1 → "Silver", i=2 → "Bronze", иначе str(i+1). `result[idx] = ...`.
3. **Время:** O(n log n) — сортировка.
4. **Память:** O(n) — результат.

**Ключевой момент:** Храним исходные индексы чтобы записать ранги в правильные позиции.
