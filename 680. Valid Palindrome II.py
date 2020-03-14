class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0; right = len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                str1 = s[left:right]
                str2 = s[left+1:right+1]
                return str1 == str1[::-1] or str2 == str2[::-1]
        return True
