class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0

        if not haystack or len(haystack) < len(needle):
            return -1
        else:
            m = len(haystack); n = len(needle)
            for i in range(m - n + 1):
                subset = haystack[i:i + n]
                if subset == needle:
                    return i
            return -1
