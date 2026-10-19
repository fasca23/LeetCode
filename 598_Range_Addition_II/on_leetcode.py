class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        # Нет операций — все элементы равны
        if not ops:
            return m * n
        
        # Минимальные координаты по всем операциям
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)
        
        # Пересечение = прямоугольник [0, min_a) × [0, min_b)
        return min_a * min_b
