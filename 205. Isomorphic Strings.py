class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        s2t = {}
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            if not char1 in s2t:
                if char2 in s2t.values():
                    return False
                s2t[char1] = char2
            else:
                if char2 != s2t[char1]:
                    return False
                else:
                    continue
        return True
