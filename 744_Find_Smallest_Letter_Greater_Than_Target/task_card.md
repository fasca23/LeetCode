---
id: find-smallest-letter-greater-than-target
title: 744. Найти наименьшую букву больше target
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/744_Find_Smallest_Letter_Greater_Than_Target
description: Дан отсортированный массив букв и target. Найти наименьшую букву строго больше target. Бинарный поиск или обход. Если нет — первая буква (циклично).
screenshots: 0
---

**Подход: Бинарный поиск**

1. **Идея:** Ищем первую букву строго больше target. Бинарный поиск: если mid <= target → ищем правее. Иначе — запоминаем, ищем левее.
2. **Логика:** `left=0, right=n-1`. Пока left <= right: `mid=(left+right)//2`. Если `letters[mid] <= target` → `left=mid+1`. Иначе `right=mid-1`. Вернуть `letters[left % n]` (циклично).
3. **Время:** O(log n) — бинарный поиск.
4. **Память:** O(1).

**Ключевой момент:** `left % n` — если все буквы ≤ target, возвращаем первую (циклично).
