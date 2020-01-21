class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dict_s = self.count(s)
            dict_t = self.count(t)
            for key in dict_s.keys():
                if not key in dict_t.keys() or (key in dict_t.keys() and dict_s[key] != dict_t[key]):
                    return False
            else:
                return True
    
    def count(self, s):
        res = dict()
        for char in s:
            if char in res.keys():
                res[char] += 1
            else:
                res[char] = 1
        return res
