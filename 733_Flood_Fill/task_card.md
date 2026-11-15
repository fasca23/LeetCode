---
id: flood-fill
title: 733. Заливка
difficulty: Easy
leetcode_url: https://leetcode.com/problems/flood-fill/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/733_Flood_Fill
description: Дана матрица image, начальная клетка (sr, sc) и новый цвет color. Залить все связанные клетки того же цвета что и стартовая. BFS или DFS.
screenshots: 0
---

**Подход: BFS с очередью**

1. **Идея:** Начинаем со стартовой клетки. Красим в новый цвет. Добавляем соседей (верх, низ, лево, право) того же исходного цвета. Повторяем.
2. **Логика:** `old = image[sr][sc]`. Если `old == color` → вернуть image (уже такой). `queue = deque([(sr, sc)])`. Пока очередь: `r, c = popleft()`. Если `image[r][c] != old` → continue. `image[r][c] = color`. Добавить 4 соседей в границах.
3. **Время:** O(n × m) — каждая клетка один раз.
4. **Память:** O(n × m) — очередь в худшем случае.

**Ключевой момент:** Проверка `old == color` предотвращает бесконечный цикл (если новый цвет совпадает со старым).
