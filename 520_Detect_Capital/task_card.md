---
id: detect-capital
title: 520. Проверка заглавных букв
difficulty: Easy
leetcode_url: https://leetcode.com/problems/detect-capital/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/520_Detect_Capital
description: Дано слово. Проверить, правильно ли использованы заглавные буквы. Правильно: все строчные, все заглавные, или только первая заглавная. Подсчёт заглавных или встроенные методы.
screenshots: 0
---

**Подход: Встроенные методы строк**

1. **Идея:** Три допустимых случая: `word.islower()`, `word.isupper()`, `word.istitle()`. Если любой из них True — правильно.
2. **Логика:** `return word.islower() or word.isupper() or word.istitle()`.
3. **Время:** O(n) — три прохода по строке.
4. **Память:** O(1).

**Ключевой момент:** `istitle()` проверяет что первая заглавная, остальные строчные. Это третий допустимый случай.
