---
id: min-cost-climbing-stairs
title: 746. Минимальная стоимость подъёма по лестнице
difficulty: Easy
leetcode_url: https://leetcode.com/problems/min-cost-climbing-stairs/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/746_Min_Cost_Climbing_Stairs
description: Дан массив cost. На ступеньке i платим cost[i] и идём на i+1 или i+2. Начать с 0 или 1. Найти минимальную стоимость до вершины. DP: dp[i] = cost[i] + min(dp[i-1], dp[i-2]).
screenshots: 0
---

**Подход: Динамическое программирование**

1. **Идея:** `dp[i]` — минимальная стоимость дойти до ступеньки i. `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`. Ответ = `min(dp[n-1], dp[n-2])` (можно закончить на предпоследней или последней).
2. **Логика:** Две переменные вместо массива: `prev2 = cost[0]`, `prev1 = cost[1]`. Для i от 2 до n: `cur = cost[i] + min(prev1, prev2)`, сдвиг.
3. **Время:** O(n) — один проход.
4. **Память:** O(1) — две переменные.

**Ключевой момент:** Начать можно с 0 или 1 ступеньки. Закончить можно на n-1 или n-2 (шаг за вершину).
