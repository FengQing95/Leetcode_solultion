class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x > 0 else -1
        x = abs(x)
        
        res = 0
        while x:
            res = res * 10 + x % 10
            x = x // 10

        return flag * res if res <= 0x7fffffff else 0
