from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        res = [1] * len(nums)
        for i in range(1, len(nums)):
            cur = nums[i]
            for j in range(i):
                if nums[j] < cur:
                    res[i] = max(res[i], res[j] + 1)

        return max(res)
