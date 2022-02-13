from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.m = dict()
        self.deq = deque()

    def get(self, key: int) -> int:
        if key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.m:
            if len(self.deq) == self.c:
                oldest = self.deq.popleft()
                del self.m[oldest]
        else:
            self.deq.remove(key)

        self.m[key] = value
        self.deq.append(key)


s = LRUCache(3)
s.put(1, 1000)
s.put(2, 2000)
s.put(3, 3000)

print(s.get(1))

s.put(4, 4000)
