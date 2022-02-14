class Solution:
    def find_hash(self, s):
        return ''.join(sorted(s))

    def group_anagrams(self, item: list[str]) -> list[list[str]]:
        answers = []
        m = {}
        for s in item:
            hashed = self.find_hash(s)
            if hashed not in m:
                m[hashed] = []
            m[hashed].append(s)
        for value in m.values():
            answers.append(value)
        return answers


s = Solution()
Result = s.group_anagrams(['tan', 'ant', 'cat', 'act'])
print(Result)
