---
id: 3sum-closest
title: 16. Ближайшая сумма трёх
difficulty: Medium
leetcode_url: https://leetcode.com/problems/3sum-closest/description/
github_url: https://github.com/fasca23/LeetCode/tree/main/16_3Sum_Closest
description: Дан массив и target. Найти сумму трёх чисел, ближайшую к target. Сортировка + два указателя: фиксируем i, для остальных ищем пару с минимальной разницей.
screenshots: 0
---

**Подход: Сортировка + два указателя**

1. **Идея:** Как 3Sum, но ищем не точное совпадение, а минимальную разницу с target. Сортируем, фиксируем i, двумя указателями двигаемся от i+1 и n-1.
2. **Логика:** Для каждой тройки считаем cur_sum. Если cur_sum == target → возвращаем. Если diff < best_diff → обновляем closest. cur_sum < target → left++. Иначе right--.
3. **Время:** O(n²) — внешний цикл O(n), внутренний O(n).
4. **Память:** O(1) — только переменные.

**Ключевой момент:** `abs(cur_sum - target)` — метрика близости. Чем меньше, тем лучше. Двигаем указатели по той же логике что в 3Sum.

```python
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        
        closest = float('inf')
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                
                if cur_sum == target:
                    return target
                
                if abs(cur_sum - target) < abs(closest - target):
                    closest = cur_sum
                
                if cur_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest