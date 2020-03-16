from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        
        res = 0
        curMax = arr[0]
        for i in range(n):
            curMax = max(curMax, arr[i])
            if curMax == i:
                res += 1        

        return res
