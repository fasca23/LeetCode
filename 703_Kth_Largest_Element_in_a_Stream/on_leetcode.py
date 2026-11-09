import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        # Min-heap из k наибольших
        self.heap = nums
        heapq.heapify(self.heap)
        
        # Оставляем только k наибольших
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        # Если val больше вершины — заменяем
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        
        # Вершина = k-й наибольший
        return self.heap[0]
