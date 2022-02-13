# LRU Cache memory
"""Here List is taken with first element as most recently used and
last element as least used and size of list_cache is pre-defined
while reading list"""


class Solution:
    def lru_cache(self, a: list[int], values: list[int]):
        m = {}

        for i in range(len(a)):
            if a[i] not in m:
                m[a[i]] = values[i]
        return m

    def get(self, key, a: list[int], m):
        if key not in a:
            return -1
        else:
            b = a.index(key)
            c = a.pop(b)
            a.reverse()
            a.append(c)
            a.reverse()

        return m[key]

    def put(self, key, value, a: list[int], m):
        if key not in m:
            b = a.pop(len(a) - 1)
            m.pop(b)
            m[key] = value
            a.reverse()
            a.append(key)
            a.reverse()
            print(m)
            return a
        else:
            b = a.index(key)
            c = a.pop(b)
            m[c] = value
            a.reverse()
            a.append(c)
            a.reverse()
            print(m)
            return a


s = Solution()
a = [1, 2, 3, 4]
values = [1000, 2000, 3000, 4000]
my_dict = s.lru_cache(a, values)
print("Initial dictionary:", my_dict)
print(s.get(3, a, my_dict))
print(s.put(5, 5000, a, my_dict))
