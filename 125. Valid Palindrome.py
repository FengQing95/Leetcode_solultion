class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        else:
            s = s.strip()
            i = 0; j = len(s) - 1
            while i < j:
                while not s[i].isalnum() and i in range(len(s) - 1):
                    i += 1
                while not s[j].isalnum() and j in range(1, len(s)):
                    j -= 1
                if i == len(s) - 1 or j == 0:
                    return True
                elif s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1; j -= 1
            return True
