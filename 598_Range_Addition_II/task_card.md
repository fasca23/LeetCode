---
id: range-addition-ii
title: 598. Сложение диапазонов II
difficulty: Easy
leetcode_url: https://leetcode.com/problems/range-addition-ii/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/598_Range_Addition_II
description: Дана матрица m×n и операции ops (пары a,b). Каждая операция увеличивает на 1 прямоугольник [0,a)×[0,b). Найти количество максимальных элементов. Ответ = min(a) × min(b) по всем ops.
screenshots: 0
---

**Подход: Минимумы по осям**

1. **Идея:** Каждая операция увеличивает верхний левый прямоугольник. Пересечение всех прямоугольников = [0, min_a) × [0, min_b). Именно там больше всего сложений.
2. **Логика:** `if not ops: return m * n`. `min_a = min(op[0] for op in ops)`, `min_b = min(op[1] for op in ops)`. Вернуть `min_a * min_b`.
3. **Время:** O(k) — проход по операциям, k = len(ops).
4. **Память:** O(1).

**Ключевой момент:** Пересечение всех прямоугольников — это прямоугольник до минимальных координат. Там всегда максимум операций.
