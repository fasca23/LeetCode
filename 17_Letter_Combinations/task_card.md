---
id: letter-combinations-of-a-phone-number
title: 17. Комбинации букв телефонного номера
difficulty: Medium
leetcode_url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/17_Letter_Combinations
description: Дана строка цифр. Вернуть все возможные комбинации букв (как на телефоне). Бэктрекинг: на каждой цифре перебираем все её буквы и рекурсивно идём дальше.
screenshots: 0
---

**Подход: Бэктрекинг (DFS с накоплением)**

1. **Идея:** Для каждой цифры есть 3-4 буквы. Строим все комбинации: берём букву для первой цифры, потом для второй, и так далее.
2. **Логика:** Таблица `phone = {'2': 'abc', '3': 'def', ...}`. Рекурсия: `backtrack(index, path)`. Если index == len(digits) — добавить path. Иначе для каждой буквы digits[index] — рекурсия с path + буква.
3. **Время:** O(4^n × n) — до 4 букв на цифру, n цифр.
4. **Память:** O(n) — глубина рекурсии.

**Ключевой момент:** Пустая строка → пустой результат. Цифры 0 и 1 не имеют букв.
