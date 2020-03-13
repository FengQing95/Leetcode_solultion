from typing import List
import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < min(coins) or not coins:
            return -1

        minCoin = min(coins)
        res = [sys.maxsize] * (amount+1)
        res[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0:
                    res[i] = min(res[i-coin] + 1, res[i])

        return -1 if res[-1] == sys.maxsize else res[-1]
