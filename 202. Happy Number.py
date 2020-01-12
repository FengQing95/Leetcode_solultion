class Solution:
    def isHappy(self, n):
        res = {}
        prev = n
        while not prev in res.keys():
            cur = self.sum_dig(prev)
            if cur == 1:
                return True
            res[prev] = cur
            prev = cur
        return False
    
    def sum_dig(self, n):
        dig = []
        while n > 0:
            cur = n % 10
            dig.append(cur)
            n = (n - cur) / 10
        return sum(i ** 2 for i in dig)
