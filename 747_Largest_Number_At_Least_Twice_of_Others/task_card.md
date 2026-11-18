---
id: largest-number-at-least-twice-of-others
title: 747. Наибольшее число, вдвое больше остальных
difficulty: Easy
leetcode_url: https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/747_Largest_Number_At_Least_Twice_of_Others
description: Дан массив. Найти индекс наибольшего числа, если оно хотя бы вдвое больше каждого другого. Иначе -1. Один проход: находим максимум и второй максимум.
screenshots: 0
---

**Подход: Максимум и второй максимум**

1. **Идея:** Находим наибольшее и второе наибольшее. Если `max >= 2 * second_max` → вернуть индекс max. Иначе -1.
2. **Логика:** Один проход: запоминаем max_val, max_idx, second_max. Для i, num: если num > max_val → second = max, max = num. Иначе если num > second → second = num. Вернуть max_idx если max >= 2*second, иначе -1.
3. **Время:** O(n) — один проход.
4. **Память:** O(1).

**Ключевой момент:** Достаточно сравнить с вторым максимумом. Если max >= 2*second_max, то max >= 2*всех остальных.
