class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        res = 0
        existed = {}
        for i in range(len(s)):
            while j < len(s):
                if s[j] not in existed:
                    existed[s[j]] = 1
                    res = max(res, j - i + 1)
                    j += 1
                else: #s[i] in existed
                    if s[i] == s[j]:
                        j += 1
                    else:
                        existed.pop(s[i])
                    break
        return res
