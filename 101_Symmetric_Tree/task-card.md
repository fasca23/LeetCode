---

id: symmetric-tree

title: 101. Симметричное дерево

difficulty: Easy

leetcode_url: https://leetcode.com/problems/symmetric-tree/description/

github_url: https://github.com/fasca23/LeetCode/tree/main/101_Symmetric_Tree

description: Дано бинарное дерево. Проверить, симметрично ли оно (зеркальное отражение). Рекурсивное сравнение левого и правого поддеревьев с перекрёстным вызовом.

screenshots: 0

---

**Подход: Рекурсивное сравнение левого и правого**

1. **Идея:** Дерево симметрично если левое поддерево = зеркальное отражение правого. Два зеркальных узла: оба None → true, одно None → false, значения равны и `(left.left, right.right)` и `(left.right, right.left)` — зеркальны.

2. **Логика:** Вспомогательная функция `mirror(a, b)`: если оба None → True. Если одно None → False. `return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)`.

3. **Время:** O(n) — каждый узел один раз.

4. **Память:** O(h) — стек рекурсии.

**Ключевой момент:** Перекрёстный вызов: `mirror(a.left, b.right)` и `mirror(a.right, b.left)` — именно это создаёт зеркальность.