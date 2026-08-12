class MyQueue:
    def __init__(self):
        # Два стека: входной и выходной
        self.in_stack = []   # для push
        self.out_stack = []  # для pop/peek
    
    def push(self, x: int) -> None:
        # Кладём во входной стек
        self.in_stack.append(x)
    
    def _transfer(self):
        # Перекладываем все элементы из входного в выходной
        # Только если выходной пуст
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
    
    def pop(self) -> int:
        # Перекладываем если нужно и забираем из выходного
        self._transfer()
        return self.out_stack.pop()
    
    def peek(self) -> int:
        # Перекладываем если нужно и смотрим на верхушку выходного
        self._transfer()
        return self.out_stack[-1]
    
    def empty(self) -> bool:
        # Очередь пуста если оба стека пусты
        return not self.in_stack and not self.out_stack
