---
id: student-attendance-record-i
title: 551. Студенческая посещаемость I
difficulty: Easy
leetcode_url: https://leetcode.com/problems/student-attendance-record-i/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/551_Student_Attendance_Record_I
description: Дана строка посещаемости (A=отсутствие, L=опоздание, P=присутствие). Студент награждается если отсутствий < 2 И нет 3 опозданий подряд. Проверяем оба условия.
screenshots: 0
---

**Подход: Два счётчика**

1. **Идея:** Считаем общее количество A (должно быть < 2) и максимальную серию L (должна быть < 3).
2. **Логика:** `count_a = 0`, `count_l = 0`, `max_l = 0`. Для ch в s: если A → `count_a += 1`. Если L → `count_l += 1`, `max_l = max(max_l, count_l)`. Иначе `count_l = 0`. Вернуть `count_a < 2 and max_l < 3`.
3. **Время:** O(n) — один проход.
4. **Память:** O(1).

**Ключевой момент:** Опоздания считаются подряд — при P счётчик L сбрасывается.
