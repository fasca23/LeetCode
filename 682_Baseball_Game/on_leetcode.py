class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        
        for op in operations:
            if op == "+":
                # Сумма двух последних
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # Удвоить последнее
                stack.append(2 * stack[-1])
            elif op == "C":
                # Удалить последнее
                stack.pop()
            else:
                # Число — добавить
                stack.append(int(op))
        
        return sum(stack)
