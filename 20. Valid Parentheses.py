class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        else:
            stack = []
            my_dict = {'(': ')', '[': ']', '{': '}'}
            for i in range(len(s)):
                char = s[i]
                if char in my_dict.keys():
                    stack.append(char)
                else:
                    if not stack or my_dict[stack[-1]] != char:
                        return False
                    else:
                        stack.pop(-1)
            return not stack
