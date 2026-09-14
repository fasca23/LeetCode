---
id: arranging-coins
title: 441. Расстановка монет
difficulty: Easy
leetcode_url: https://leetcode.com/problems/arranging-coins/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/441_Arranging_Coins
description: Дано n монет. Строим лестницу: 1-й ряд 1 монета, 2-й 2, 3-й 3... Сколько полных рядов получится? Бинарный поиск или формула k(k+1)/2 ≤ n.
screenshots: 0
---

**Подход: Бинарный поиск**

1. **Идея:** Сумма первых k рядов = k(k+1)/2. Ищем максимальное k, при котором сумма ≤ n.
2. **Логика:** `left=1, right=n`. Пока left <= right: `mid=(left+right)//2`. Если `mid*(mid+1)//2 <= n` → `result=mid`, `left=mid+1`. Иначе `right=mid-1`.
3. **Время:** O(log n) — бинарный поиск.
4. **Память:** O(1).

**Ключевой момент:** Формула суммы арифметической прогрессии: 1+2+...+k = k(k+1)/2. Ответ — максимальное k где эта сумма ≤ n.
