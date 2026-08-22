---
id: range-sum-query-immutable
title: 303. Сумма диапазона (неизменяемый массив)
difficulty: Easy
leetcode_url: https://leetcode.com/problems/range-sum-query-immutable/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/303_Range_Sum_Query_Immutable
description: Дан массив. Много запросов sumRange(i, j). Префиксные суммы: prefix[i] = сумма элементов до i. Ответ: prefix[j+1] - prefix[i] за O(1) на запрос.
screenshots: 0
---

**Подход: Префиксные суммы**

1. **Идея:** Заранее считаем суммы до каждого индекса: prefix[i] = сумма nums[0..i-1]. Тогда sumRange(i, j) = prefix[j+1] - prefix[i].
2. **Логика:** В конструкторе: `prefix = [0]`, для каждого num: `prefix.append(prefix[-1] + num)`. В sumRange: `return prefix[j+1] - prefix[i]`.
3. **Время:** O(n) на построение, O(1) на каждый запрос.
4. **Память:** O(n) — массив префиксов.

**Ключевой момент:** Без префиксов каждый запрос был бы O(n). С префиксами — O(1). Выгодно когда запросов много.
