class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        start = 0; end = x
        while start + 1 < end:
            cur = start + (end - start) // 2
            if cur * cur < x:
                start = cur
            elif cur * cur > x:
                end = cur
            else:
                return cur
        if start == end:
            return end
        else:
            return start
