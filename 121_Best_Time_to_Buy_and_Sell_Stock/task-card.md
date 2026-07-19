
---
id: best-time-to-buy-and-sell-stock
title: 121. Лучшее время для покупки и продажи
difficulty: Easy
leetcode_url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/121_Best_Time_to_Buy_and_Sell_Stock
description: Дан массив цен. Найти максимальную прибыль от одной сделки (купить → продать). Один проход: отслеживаем минимум и максимум прибыли.
screenshots: 0
---

**Подход: Один проход с отслеживанием минимума**

1. **Идея:** Идём по ценам. На каждом шаге знаем минимальную цену до текущего дня. Прибыль = текущая цена − минимум. Обновляем максимум прибыли.
2. **Логика:** `min_price = inf`, `max_profit = 0`. Для каждой цены: `min_price = min(min_price, price)`, `max_profit = max(max_profit, price - min_price)`.
3. **Время:** O(n) — один проход.
4. **Память:** O(1) — две переменные.

**Ключевой момент:** Нельзя продать раньше чем купить. Поэтому минимум обновляем до расчёта прибыли.
