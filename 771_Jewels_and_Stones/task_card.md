---
id: jewels-and-stones
title: 771. Камни и драгоценности
difficulty: Easy
leetcode_url: https://leetcode.com/problems/jewels-and-stones/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/771_Jewels_and_Stones
description: Даны строки jewels (типы драгоценностей) и stones (камни). Посчитать сколько камней являются драгоценностями. Set из jewels + проход по stones.
screenshots: 0
---

**Подход: Set + подсчёт**

1. **Идея:** Множество букв-драгоценностей. Проходим по stones: если камень в set — считаем.
2. **Логика:** `jewel_set = set(jewels)`. `count = 0`. Для stone в stones: если stone в jewel_set → `count += 1`. Вернуть count.
3. **Время:** O(n + m) — set + проход.
4. **Память:** O(1) — set из 52 букв максимум.

**Ключевой момент:** Set даёт O(1) проверку. Порядок не важен, важны только типы.
