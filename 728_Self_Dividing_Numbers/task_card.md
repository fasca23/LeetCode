---
id: self-dividing-numbers
title: 728. Самоделящиеся числа
difficulty: Easy
leetcode_url: https://leetcode.com/problems/self-dividing-numbers/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/728_Self_Dividing_Numbers
description: Даны left и right. Найти все числа в диапазоне, которые делятся на каждую свою цифру без остатка. Цифра 0 — число не подходит.
screenshots: 0
---

**Подход: Перебор с проверкой цифр**

1. **Идея:** Для каждого числа в [left, right] проверяем: делится ли на каждую свою цифру. Если есть 0 — не подходит.
2. **Логика:** `result = []`. Для num в range(left, right+1): `if all(int(d) != 0 and num % int(d) == 0 for d in str(num))` → добавить.
3. **Время:** O(n × k) — n чисел, k цифр в каждом.
4. **Память:** O(1) — не считая результата.

**Ключевой момент:** Если в числе есть 0 — делить на него нельзя. Такие числа сразу отбрасываются.
