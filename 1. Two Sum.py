class Solution:
    def twoSum(self, nums, target: int):
        existed = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in existed:
                return [i, existed[target - num]]
            else:
                existed[num] = i
