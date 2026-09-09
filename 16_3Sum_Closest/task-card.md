---
id: 3sum-closest
title: 16. Ближайшая сумма трёх
difficulty: Medium
leetcode_url: https://leetcode.com/problems/3sum-closest/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/16_3Sum_Closest
description: Дан массив и target. Найти сумму трёх чисел, ближайшую к target. Сортировка + два указателя: фиксируем i, для остальных ищем пару с минимальной разницей.
screenshots: 0
---

**Подход: Сортировка + два указателя**

1. **Идея:** Как 3Sum, но ищем не точное совпадение, а минимальную разницу с target. Сортируем, фиксируем i, двумя указателями двигаемся от i+1 и n-1.
2. **Логика:** Для каждой тройки считаем cur_sum. Если cur_sum == target → возвращаем. Если diff < best_diff → обновляем closest. cur_sum < target → left++. Иначе right--.
3. **Время:** O(n²) — внешний цикл O(n), внутренний O(n).
4. **Память:** O(1) — только переменные.

**Ключевой момент:** `abs(cur_sum - target)` — метрика близости. Чем меньше, тем лучше. Двигаем указатели по той же логике что в 3Sum.
