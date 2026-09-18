---
id: hamming-distance
title: 461. Расстояние Хэмминга
difficulty: Easy
leetcode_url: https://leetcode.com/problems/hamming-distance/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/461_Hamming_Distance
description: Даны два числа x и y. Расстояние Хэмминга — количество позиций где биты различаются. XOR даёт 1 на различающихся битах, считаем единицы.
screenshots: 0
---

**Подход: XOR + подсчёт битов**

1. **Идея:** XOR двух чисел даёт 1 на позициях где биты разные. Считаем количество единиц в результате.
2. **Логика:** `xor = x ^ y`. `count = 0`. Пока xor: `xor &= xor - 1`, `count += 1`. Вернуть count.
3. **Время:** O(k) — k = количество различающихся битов.
4. **Память:** O(1).

**Ключевой момент:** `n & (n-1)` обнуляет младший единичный бит. Считаем сколько раз можем применить.
