---
id: add-strings
title: 415. Сложение строк
difficulty: Easy
leetcode_url: https://leetcode.com/problems/add-strings/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/415_Add_Strings
description: Даны две строки с числами. Вернуть их сумму в виде строки. Складываем посимвольно с конца, как в столбик, с переносом.
screenshots: 0
---

**Подход: Поразрядное сложение с конца**

1. **Идея:** Складываем цифры с конца обеих строк + перенос. Как сложение в столбик. Результат собираем в обратном порядке.
2. **Логика:** `i, j = len-1, len-1`. `carry = 0`. Пока i >= 0 или j >= 0 или carry: `total = int(num1[i]) + int(num2[j]) + carry`. `result.append(str(total % 10))`. `carry = total // 10`.
3. **Время:** O(max(n, m)).
4. **Память:** O(max(n, m)).

**Ключевой момент:** Нельзя использовать int() для всей строки — числа могут быть очень большими (сотни цифр).
