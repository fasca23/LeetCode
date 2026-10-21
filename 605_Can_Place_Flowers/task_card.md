---
id: can-place-flowers
title: 605. Можно ли посадить цветы
difficulty: Easy
leetcode_url: https://leetcode.com/problems/can-place-flowers/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/605_Can_Place_Flowers
description: Дан массив flowerbed (0 свободно, 1 занято) и число n. Можно ли посадить n цветов так, чтобы не было соседних? Один проход: если текущая и обе соседние пусты — сажаем.
screenshots: 0
---

**Подход: Жадный проход с проверкой соседей**

1. **Идея:** Идём по грядке. Цветок можно посадить, если текущая клетка 0 И левая (или край) 0 И правая (или край) 0. Сажаем и идём через одну.
2. **Логика:** Для i от 0 до n-1: `left_ok = (i == 0 or flowerbed[i-1] == 0)`, `right_ok = (i == len-1 or flowerbed[i+1] == 0)`. Если `flowerbed[i] == 0 and left_ok and right_ok`: `flowerbed[i] = 1`, `n -= 1`. Если n == 0 → True.
3. **Время:** O(n) — один проход.
4. **Память:** O(1).

**Ключевой момент:** Края считаются пустыми (за границей массива цветов нет). Жадная посадка слева направо оптимальна.
