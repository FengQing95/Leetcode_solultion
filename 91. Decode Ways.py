class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 0 if s == "0" else 1

        res = [1] * len(s)
        res[0] = 0 if s[0] == "0" else 1
        for i in range(1, len(s)):
            cur = s[i]
            prev = s[i-1]
            if cur == "0":
                if prev in ["1", "2"]:
                    res[i] = res[i-2]
                else:
                    return 0
            elif (prev == '1') or (prev == '2' and cur < '7'):
                res[i] = res[i-1] + res[i-2]
            else:
                res[i] = res[i-1]
        return res[-1]
