---
id: valid-palindrome
title: 125. Валидный палиндром
difficulty: Easy
leetcode_url: https://leetcode.com/problems/valid-palindrome/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/125_Valid_Palindrome
description: Дана строка. Проверить, является ли она палиндромом (только буквы и цифры, регистр не важен). Два указателя: слева и справа, пропускаем не-буквоцифры, сравниваем lowercase.
screenshots: 0
---

**Подход: Два указателя**

1. **Идея:** Указатели left и right идут навстречу. Пропускаем всё кроме букв и цифр. Сравниваем без учёта регистра. Если не равны → False.
2. **Логика:** `left=0, right=n-1`. Пока left < right: пропустить не-alnum слева, пропустить справа. Если `s[left].lower() != s[right].lower()` → False. left++, right--.
3. **Время:** O(n) — один проход.
4. **Память:** O(1) — два указателя.

**Ключевой момент:** `isalnum()` проверяет что символ — буква или цифра. Регистр игнорируем через `.lower()`.
