---
id: robot-return-to-origin
title: 657. Робот возвращается в начало
difficulty: Easy
leetcode_url: https://leetcode.com/problems/robot-return-to-origin/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/657_Robot_Return_to_Origin
description: Дана строка команд (U/D/L/R). Робот начинает в (0,0). Вернулся ли он в начало? Считаем смещения: U/D меняют y, L/R меняют x. Оба должны быть 0.
screenshots: 0
---

**Подход: Подсчёт смещений**

1. **Идея:** Считаем итоговое смещение по x и y. U → y+1, D → y-1, R → x+1, L → x-1. В начале (0,0) → вернулся если x=0 и y=0.
2. **Логика:** `x = y = 0`. Для ch в moves: U → y+=1, D → y-=1, R → x+=1, L → x-=1. Вернуть `x == 0 and y == 0`.
3. **Время:** O(n) — один проход.
4. **Память:** O(1).

**Ключевой момент:** Не важна последовательность команд — только итоговое смещение. Порядок не влияет на возврат в начало.
