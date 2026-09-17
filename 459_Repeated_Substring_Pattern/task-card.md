---
id: repeated-substring-pattern
title: 459. Повторяющийся подстроковый шаблон
difficulty: Easy
leetcode_url: https://leetcode.com/problems/repeated-substring-pattern/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/459_Repeated_Substring_Pattern
description: Дана строка s. Проверить, можно ли её составить повторением подстроки. Трюк: s + s без первого и последнего символа содержит s, если s повторяющаяся.
screenshots: 0
---

**Подход: Трюк с удвоением строки**

1. **Идея:** Если s = "abcabc" (повтор "abc"), то s + s = "abcabcabcabc". Убираем первый и последний символ: "bcabcabcab". Внутри содержится s = "abcabc".
2. **Логика:** `return s in (s + s)[1:-1]`.
3. **Время:** O(n) — поиск подстроки.
4. **Память:** O(n) — удвоенная строка.

**Ключевой момент:** Трюк работает потому что удвоение сдвигает границу повторов, и исходная строка находится внутри.
