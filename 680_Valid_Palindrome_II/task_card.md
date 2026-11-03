---
id: valid-palindrome-ii
title: 680. Валидный палиндром II
difficulty: Easy
leetcode_url: https://leetcode.com/problems/valid-palindrome-ii/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/680_Valid_Palindrome_II
description: Дана строка. Можно удалить максимум один символ. Проверить, будет ли палиндром. Два указателя: при несовпадении пробуем пропустить левый или правый.
screenshots: 0
---

**Подход: Два указателя с одной попыткой**

1. **Идея:** Идём двумя указателями. При несовпадении пробуем два варианта: пропустить левый символ или правый. Если любой даёт палиндром — True.
2. **Логика:** `left, right = 0, n-1`. Пока left < right: если `s[left] != s[right]` → проверить `is_pal(left+1, right)` или `is_pal(left, right-1)`. Иначе left++, right--.
3. **Время:** O(n) — два прохода в худшем случае.
4. **Память:** O(1).

**Ключевой момент:** Удалить можно только один символ. При первом несовпадении — выбор: удалить левый или правый.
