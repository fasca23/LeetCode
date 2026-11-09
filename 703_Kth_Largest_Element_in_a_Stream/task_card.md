---
id: kth-largest-element-in-a-stream
title: 703. K-й наибольший элемент в потоке
difficulty: Easy
leetcode_url: https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/703_Kth_Largest_Element_in_a_Stream
description: Дан поток чисел и k. После каждого добавления возвращать k-й наибольший элемент. Min-heap размера k: вершина = k-й наибольший.
screenshots: 0
---

**Подход: Min-heap размера k**

1. **Идея:** Держим кучу из k наибольших элементов. Вершина min-heap = наименьший из них = k-й наибольший.
2. **Логика:** `__init__`: heapify первых элементов, оставить k наибольших. `add(val)`: если `val > heap[0]` → заменить вершину. Вернуть `heap[0]`.
3. **Время:** add — O(log k). init — O(n log k).
4. **Память:** O(k) — куча.

**Ключевой момент:** Min-heap из k элементов: вершина — минимальный среди k наибольших = k-й наибольший.
