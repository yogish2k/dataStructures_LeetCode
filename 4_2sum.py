# 4 list integers with A+B = x C+D = -x (Such that A+B+C+D = 0)

class Solution:
    def four_sum(self, a: list, b: list, c: list, d: list) -> int:
        m = {}
        ans = 0
        for i in range(len(a)):
            for j in range(len(b)):
                sum = a[i] + b[j]
                if sum not in m:
                    m[sum] = m.get(sum, 0) + 1
        for k in range(len(c)):
            for e in range(len(d)):
                target = -(c[k] + d[e])
                if target in m.keys():
                    ans = ans + m[target]
        return ans


s = Solution()
result = s.four_sum([1, 2], [-2, -1], [-1, 2], [0, 2])
print(result)
