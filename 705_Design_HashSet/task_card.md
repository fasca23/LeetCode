---
id: design-hashset
title: 705. Реализация HashSet
difficulty: Easy
leetcode_url: https://leetcode.com/problems/design-hashset/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/705_Design_HashSet
description: Реализовать HashSet без встроенных хэш-структур. add, remove, contains. Массив корзин (bucket), хэш-функция key % size, цепочки для коллизий.
screenshots: 0
---

**Подход: Массив корзин + цепочки**

1. **Идея:** Массив из N корзин. Хэш = key % N определяет корзину. В каждой корзине — список для коллизий. add/remove/contains — идём в корзину и ищем.
2. **Логика:** `buckets = [[] for _ in range(1000)]`. `add`: `idx = key % 1000`, если key нет в buckets[idx] — append. `remove`: удалить из списка. `contains`: проверить наличие.
3. **Время:** в среднем O(1), в худшем O(n) при коллизиях.
4. **Память:** O(n) — все элементы.

**Ключевой момент:** Хэш-функция распределяет элементы по корзинам. Цепочки (списки) обрабатывают коллизии.
