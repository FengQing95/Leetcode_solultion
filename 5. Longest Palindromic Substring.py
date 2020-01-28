class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        else:
            ptr = 0
            res = s[0]
            n = len(s)

            while ptr < n - 2:
                if s[ptr] != s[ptr + 2] and s[ptr] != s[ptr + 1]:
                    ptr += 1
                    continue

                if s[ptr] == s[ptr +2]:
                    left = ptr; right = ptr + 2
                    res = self.find_max(left, right, s, res)
                if s[ptr] == s[ptr + 1]:
                    left = ptr; right = ptr + 1
                    res = self.find_max(left, right, s, res)                
                ptr += 1

            if len(res) == 1 and s[ptr] == s[ptr + 1]:
                res = s[ptr:]
            return res
    
    def find_max(self, left, right, s, res_former):
        n = len(s)
        res = s[left:right + 1]
        while left > 0 and right < n -1 and s[left - 1] == s[right + 1]:
            left -= 1
            right += 1
            if right - left + 1 > len(res):
                res = s[left:right + 1]
        return res if right - left + 1 > len(res_former) else res_former
                    
