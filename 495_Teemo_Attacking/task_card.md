---
id: teemo-attacking
title: 495. Атака Тимо
difficulty: Easy
leetcode_url: https://leetcode.com/problems/teemo-attacking/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/495_Teemo_Attacking
description: Дан массив времени атак и длительность отравления. Найти общее время отравления. Если атаки перекрываются — считаем один раз. Сумма min(duration, разница между атаками).
screenshots: 0
---

**Подход: Сумма неперекрывающихся интервалов**

1. **Идея:** Каждая атака отравляет на duration секунд. Но если следующая атака раньше — отравление продлевается. Считаем min(duration, gap) для каждой атаки кроме последней.
2. **Логика:** `total = 0`. Для i от 0 до n-2: `total += min(duration, timeSeries[i+1] - timeSeries[i])`. В конце `total += duration`.
3. **Время:** O(n) — один проход.
4. **Память:** O(1).

**Ключевой момент:** Последняя атака всегда даёт полный duration. Предыдущие — либо duration, либо до следующей атаки.
