---
id: reverse-string
title: 344. Обратная строка
difficulty: Easy
leetcode_url: https://leetcode.com/problems/reverse-string/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/344_Reverse_String
description: Дан массив символов. Развернуть его на месте. Два указателя: слева и справа, меняем местами пока не встретятся.
screenshots: 0
---

**Подход: Два указателя**

1. **Идея:** Указатели left и right идут навстречу. Меняем местами s[left] и s[right], сдвигаем к центру. Повторяем пока left < right.
2. **Логика:** `left=0, right=n-1`. Пока left < right: `s[left], s[right] = s[right], s[left]`, `left += 1`, `right -= 1`.
3. **Время:** O(n) — один проход половины массива.
4. **Память:** O(1) — на месте.

**Ключевой момент:** Обмен на месте без доп. памяти. Python позволяет менять местами в одну строку.
