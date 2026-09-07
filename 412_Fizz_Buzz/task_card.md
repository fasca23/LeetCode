---
id: fizz-buzz
title: 412. Fizz Buzz
difficulty: Easy
leetcode_url: https://leetcode.com/problems/fizz-buzz/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/412_Fizz_Buzz
description: Дано число n. Для чисел от 1 до n: кратно 3 → "Fizz", кратно 5 → "Buzz", кратно обоим → "FizzBuzz", иначе само число. Простой цикл с проверками.
screenshots: 0
---

**Подход: Цикл с проверками**

1. **Идея:** Для каждого числа проверяем кратность. Порядок важен: сначала FizzBuzz (кратно 15), потом Fizz, потом Buzz.
2. **Логика:** Для i от 1 до n: если i % 15 == 0 → "FizzBuzz". Если i % 3 == 0 → "Fizz". Если i % 5 == 0 → "Buzz". Иначе str(i).
3. **Время:** O(n) — один проход.
4. **Память:** O(n) — массив результата.

**Ключевой момент:** Проверка i % 15 должна быть первой. Иначе FizzBuzz перехватится проверкой Fizz (для 15: i % 3 == 0).
