class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.read(self.countAndSay(n - 1))
    
    def read(self, s: str) -> str:
        res = ""
        left = 0
        while left < len(s):
            right = left
            count = 1
            while right < len(s) - 1:
                if s[left] == s[right + 1]:
                    right += 1
                    count += 1
                else:
                    break
            res = res + str(count) + s[left]
            left = right + 1
        return res
