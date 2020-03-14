class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        minList = [nums[0]] * n
        maxList = [nums[0]] * n
        for i in range(1, n):
            cur = nums[i]
            minList[i] = min(cur, cur * minList[i-1], cur * maxList[i-1])
            maxList[i] = max(cur, cur * maxList[i-1], cur * minList[i-1])

        return max(maxList)
