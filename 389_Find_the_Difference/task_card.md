---
id: find-the-difference
title: 389. Найти отличие
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-the-difference/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/389_Find_the_Difference
description: Даны строки s и t. t получена из s добавлением одного символа. Найти этот символ. XOR всех символов: парные обнулятся, останется добавленный.
screenshots: 0
---

**Подход: XOR всех символов**

1. **Идея:** XOR всех символов s и t. Все символы которые есть в обоих строках встретятся дважды и обнулятся (a ^ a = 0). Останется только добавленный символ.
2. **Логика:** `result = 0`. Для ch в s: `result ^= ord(ch)`. Для ch в t: `result ^= ord(ch)`. Вернуть `chr(result)`.
3. **Время:** O(n) — один проход по обеим строкам.
4. **Память:** O(1) — одна переменная.

**Ключевой момент:** XOR коммутативен и a ^ a = 0. Все парные обнуляются, остаётся уникальный символ.
