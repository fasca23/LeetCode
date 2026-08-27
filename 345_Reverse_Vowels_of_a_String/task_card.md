---
id: reverse-vowels-of-a-string
title: 345. Обратные гласные в строке
difficulty: Easy
leetcode_url: https://leetcode.com/problems/reverse-vowels-of-a-string/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/345_Reverse_Vowels_of_a_String
description: Дана строка. Развернуть только гласные буквы, согласные остаются на местах. Два указателя: ищем гласные слева и справа, меняем местами.
screenshots: 0
---

**Подход: Два указателя**

1. **Идея:** Указатели left и right ищут гласные с обоих концов. Нашли обе — меняем местами. Пропускаем согласные.
2. **Логика:** `vowels = set("aeiouAEIOU")`. `left=0, right=n-1`. Пока left < right: если s[left] не гласная → left++. Если s[right] не гласная → right--. Иначе меняем местами.
3. **Время:** O(n) — один проход.
4. **Память:** O(n) — строка → список для изменения.

**Ключевой момент:** Гласные и в верхнем и нижнем регистре. Согласные не двигаются.
