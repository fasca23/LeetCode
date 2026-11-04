---
id: baseball-game
title: 682. Бейсбольный матч
difficulty: Easy
leetcode_url: https://leetcode.com/problems/baseball-game/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/682_Baseball_Game
description: Дан список операций. Число — добавить очки. "+" — сумма двух последних. "D" — удвоить последнее. "C" — удалить последнее. Вернуть сумму всех очков. Стек.
screenshots: 0
---

**Подход: Стек**

1. **Идея:** Стек хранит текущие очки. Число — push. "+" — push(последние два). "D" — push(2*последнее). "C" — pop. В конце сумма стека.
2. **Логика:** `stack = []`. Для op в operations: если число → `stack.append(int(op))`. "+" → `stack.append(stack[-1] + stack[-2])`. "D" → `stack.append(2 * stack[-1])`. "C" → `stack.pop()`. Вернуть `sum(stack)`.
3. **Время:** O(n) — один проход.
4. **Память:** O(n) — стек.

**Ключевой момент:** Стек идеален: операции работают с последними элементами. "C" удаляет последний, "+" и "D" смотрят на последние.
