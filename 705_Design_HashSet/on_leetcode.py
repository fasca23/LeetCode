class MyHashSet:
    def __init__(self):
        # Массив корзин
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key: int) -> int:
        # Хэш-функция: key % size
        return key % self.size
    
    def add(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        if key not in bucket:
            bucket.append(key)
    
    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        if key in bucket:
            bucket.remove(key)
    
    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.buckets[idx]
