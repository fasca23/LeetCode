class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key: int) -> int:
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        # Ищем существующий ключ
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value  # обновляем
                return
        # Не нашли — добавляем
        bucket.append([key, value])
    
    def get(self, key: int) -> int:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return -1
    
    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return
