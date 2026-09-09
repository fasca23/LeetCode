---
id: two-sum
title: 1. Два слагаемых
difficulty: Easy
leetcode_url: https://leetcode.com/problems/two-sum/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/1_Two_Sum
description: Дан массив nums и число target. Найти индексы двух элементов, которые в сумме дают target. Ровно одно решение, нельзя использовать один элемент дважды.
screenshots: 7
---

**Подход: Хеш-таблица (словарь)**

1. **Идея:** Проходим по массиву один раз, сохраняя уже просмотренные числа в словаре (значение → индекс).
2. **Логика:** Для каждого числа `nums[i]` вычисляем `complement = target - nums[i]`. Если complement уже есть в словаре, значит мы нашли пару.
3. **Почему работает:** Хеш-таблица обеспечивает O(1) поиск, что даёт общую сложность O(n) вместо O(n²) при переборе.
4. **Время:** O(n) — один проход по массиву.
5. **Память:** O(n) — в худшем случае храним все элементы в словаре.

**Ключевой момент:** Мы возвращаем индексы `[dict[complement], i]`, где dict[complement] — индекс ранее встреченного числа.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            need = target - num       # сколько не хватает до target
            if need in seen:          # уже встречали?
                return [seen[need], i] # нашли пару
            seen[num] = i             # запоминаем текущий
