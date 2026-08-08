class MyStack:
    def __init__(self):
        # Одна очередь
        self.q = deque()
    
    def push(self, x: int) -> None:
        # Добавляем элемент в конец очереди
        self.q.append(x)
        
        # Перекладываем все элементы перед ним в конец
        # Новый элемент становится первым (верхушкой стека)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self) -> int:
        # Верхушка стека = начало очереди
        return self.q.popleft()
    
    def top(self) -> int:
        # Верхушка стека = первый элемент очереди
        return self.q[0]
    
    def empty(self) -> bool:
        return len(self.q) == 0
