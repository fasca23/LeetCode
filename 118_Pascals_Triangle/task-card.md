---

id: pascals-triangle

title: 118. Треугольник Паскаля

difficulty: Easy

leetcode_url: https://leetcode.com/problems/pascals-triangle/description/

github_url: https://github.com/fasca23/LeetCode/tree/main/118_Pascals_Triangle

description: Дано число строк numRows. Построить треугольник Паскаля. Каждый элемент = сумма двух верхних. Итеративное построение строка за строкой.

screenshots: 0

---

**Подход: Итеративное построение**

1. **Идея:** Первая строка = [1]. Каждая следующая: по краям 1, в середине `row[j] = prev[j-1] + prev[j]`. Повторяем numRows раз.

2. **Логика:** `result = [[1]]`. Для i от 1 до numRows-1: `prev = result[-1]`, `row = [1]`, для j от 1 до len(prev)-1: `row.append(prev[j-1] + prev[j])`, `row.append(1)`, `result.append(row)`.

3. **Время:** O(n²) — где n = numRows, общее число элементов = n(n+1)/2.

4. **Память:** O(n²) — хранение всего треугольника.

**Ключевой момент:** Каждый внутренний элемент = сумма двух элементов сверху-слева и сверху-справа. Края всегда 1.