class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        else:
            res = 0
            res_cur = 0
            ptr = len(s) - 1
            while ptr >= 0:
                if s[ptr]== " ":
                    res_cur = 0
                else:
                    res_cur += 1
                    res = res_cur
                
                if res > res_cur:
                    return res
                ptr -= 1
            return res
