from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        res = []
        intervals = sorted(intervals, key = lambda x: x[0])
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1] = [min(res[-1][0], interval[0]), max(res[-1][1], interval[1])]
        return res
