---
id: contains-duplicate-ii
title: 219. Содержит дубликаты II
difficulty: Easy
leetcode_url: https://leetcode.com/problems/contains-duplicate-ii/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/219_Contains_Duplicate_II
description: Дан массив и число k. Есть ли два одинаковых элемента на расстоянии не более k? Словарь: значение → последний индекс. Если встретили снова и разница ≤ k → True.
screenshots: 0
---

**Подход: Словарь (значение → последний индекс)**

1. **Идея:** Храним для каждого значения его последнюю позицию. Когда встречаем снова — проверяем разницу индексов. Если ≤ k → нашли.
2. **Логика:** `last = {}`. Для i, num: если num уже в last и `i - last[num] <= k` → True. Иначе `last[num] = i`.
3. **Время:** O(n) — один проход.
4. **Память:** O(n) — словарь.

**Ключевой момент:** Словарь хранит только последний индекс. Если разница > k, старое значение уже бесполезно — обновляем индекс.
