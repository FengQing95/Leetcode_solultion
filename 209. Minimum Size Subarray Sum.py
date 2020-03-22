from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sum = nums[0] 
        res = len(nums) + 1
        j = 0

        for i in range(len(nums)):
            while j < len(nums):
                if sum >= s:
                    res = min(res, j - i + 1)
                    break
                elif j + 1 < len(nums):
                    j += 1
                    sum += nums[j]
                else:
                    break
            sum -= nums[i]
        return 0 if res == len(nums)+1 else res  
