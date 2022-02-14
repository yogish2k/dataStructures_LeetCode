class Solution:
    def min_window(self, s: str, t: str):
        len1 = len(s)
        len2 = len(t)

        if len1 < len2:
            return ""
        hashPat = {}
        hashStr = {}

        for i in range(len2):
            if hashPat.get(t[i]) is None:
                hashPat[t[i]] = 0
            hashPat[t[i]] += 1

        count = 0
        left = 0
        startIndex = -1
        minLen = float("inf")

        for right in range(0, len1):
            if hashStr.get(s[right]) is None:
                hashStr[s[right]] = 0
            hashStr[s[right]] += 1

            if hashPat.get(s[right]) is None:
                hashPat[s[right]] = 0

            if hashStr.get(s[right]) <= hashPat.get(s[right]):
                count += 1

            if count == len2:
                while hashStr.get(s[left]) > hashPat.get(s[left]):
                    hashStr[s[left]] -= 1
                    left += 1
                windowLen = right - left + 1
                if minLen > windowLen:
                    minLen = windowLen
                    startIndex = left

        if startIndex == -1:
            return "Pattern doesn't exists in string"
        return s[startIndex:startIndex + minLen]


s = Solution()
answer = s.min_window('aabcseac', 'ceaad')
print(answer)
