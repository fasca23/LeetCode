---
id: construct-the-rectangle
title: 492. Построить прямоугольник
difficulty: Easy
leetcode_url: https://leetcode.com/problems/construct-the-rectangle/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/492_Construct_the_Rectangle
description: Дана площадь area. Найти прямоугольник [L, W] где L×W = area, L ≥ W, разница L-W минимальна. Идём от √area вниз, ищем первый делитель.
screenshots: 0
---

**Подход: Перебор от √area**

1. **Идея:** Чтобы L и W были близки, начинаем с √area. Идём вниз, ищем первый делитель. Это будет W. L = area / W.
2. **Логика:** `for w in range(int(area**0.5), 0, -1): if area % w == 0: return [area // w, w]`.
3. **Время:** O(√n) — в худшем случае проходим до 1.
4. **Память:** O(1).

**Ключевой момент:** Ближайшие делители — около √area. Начинаем оттуда, первый найденный делитель даёт минимальную разницу.
