class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        else:
            res = 0
            left = right = prices[0]
            flag = True

            for i in range(1, len(prices)):
                cur = prices[i]
                flag = False if cur < left else True
                left = min(left, cur)
                if flag:
                    if cur - left > res:
                        right = cur
                        res = right - left
            return res
