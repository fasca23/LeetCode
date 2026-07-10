---

id: maximum-depth-of-binary-tree

title: 104. Максимальная глубина дерева

difficulty: Easy

leetcode_url: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

github_url: https://github.com/fasca23/LeetCode/tree/main/104_Maximum_Depth

description: Дано бинарное дерево. Найти максимальную глубину (число узлов от корня до самого дальнего листа). Рекурсия: 1 + max(глубина левого, глубина правого).

screenshots: 0

---

**Подход: Рекурсивный подсчёт**

1. **Идея:** Глубина пустого дерева = 0. Глубина узла = 1 + max(глубина левого, глубина правого).

2. **Логика:** `if not root: return 0`. `return 1 + max(maxDepth(root.left), maxDepth(root.right))`.

3. **Время:** O(n) — каждый узел один раз.

4. **Память:** O(h) — стек рекурсии.

**Ключевой момент:** База рекурсии — пустой узел возвращает 0. Лист вернёт 1 (0 слева + 0 справа + 1).