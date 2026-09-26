---
id: keyboard-row
title: 500. Ряд клавиатуры
difficulty: Easy
leetcode_url: https://leetcode.com/problems/keyboard-row/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/500_Keyboard_Row
description: Дан массив слов. Вернуть слова, которые можно набрать буквами одного ряда клавиатуры. Три множества для трёх рядов, проверяем что все буквы слова из одного.
screenshots: 0
---

**Подход: Три множества рядов**

1. **Идея:** Каждый ряд клавиатуры — множество букв. Слово подходит если все его буквы принадлежат одному множеству.
2. **Логика:** `row1 = set("qwertyuiop")`, `row2 = set("asdfghjkl")`, `row3 = set("zxcvbnm")`. Для каждого слова: `letters = set(word.lower())`. Если `letters <= row1` или `letters <= row2` или `letters <= row3` → добавляем.
3. **Время:** O(n × m) — n слов, m букв в каждом.
4. **Память:** O(1) — три множества фиксированного размера.

**Ключевой момент:** `set(word) <= row` — проверка подмножества. Все буквы слова должны быть в одном ряду.
