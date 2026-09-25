---
id: next-greater-element-i
title: 496. Следующий больший элемент I
difficulty: Easy
leetcode_url: https://leetcode.com/problems/next-greater-element-i/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/496_Next_Greater_Element_I
description: Даны массивы nums1 и nums2 (nums1 — подмножество nums2). Для каждого числа из nums1 найти следующее большее в nums2 справа. Монотонный стек + словарь.
screenshots: 0
---

**Подход: Монотонный стек + словарь**

1. **Идея:** Идём по nums2. Держим стек убывающих чисел. Когда встречаем число больше верхушки стека — для верхушки это и есть следующий больший. Записываем в словарь.
2. **Логика:** `stack = []`, `next_greater = {}`. Для num в nums2: пока стек не пуст и `stack[-1] < num`: `next_greater[stack.pop()] = num`. Push num в стек. Для nums1: `next_greater.get(x, -1)`.
3. **Время:** O(n + m) — каждый элемент push/pop один раз.
4. **Память:** O(n) — стек + словарь.

**Ключевой момент:** Стек хранит числа, для которых ещё не нашли следующий больший. Новое число "закрывает" все меньшие в стеке.
