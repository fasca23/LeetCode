---
id: distribute-candies
title: 575. Раздача конфет
difficulty: Easy
leetcode_url: https://leetcode.com/problems/distribute-candies/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/575_Distribute_Candies
description: Дан массив типов конфет. Разделить поровну между братом и сестрой. Сестра хочет максимум разных типов. Ответ = min(уникальных типов, n/2).
screenshots: 0
---

**Подход: Математическое наблюдение**

1. **Идея:** Сестра получит n/2 конфет. Максимум разных типов = min(количество уникальных, n/2).
2. **Логика:** `unique = len(set(candyType))`. `half = len(candyType) // 2`. Вернуть `min(unique, half)`.
3. **Время:** O(n) — построение set.
4. **Память:** O(n) — set.

**Ключевой момент:** Если уникальных типов больше чем n/2 — сестра возьмёт n/2 разных. Если меньше — все уникальные.
