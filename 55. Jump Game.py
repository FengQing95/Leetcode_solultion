class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        reach = 0
        n = len(nums)
        for i in range(n):
            reach = max(reach, i + nums[i]) if reach >= i else reach
            if reach >= n -1:
                return True
            print(reach)

        return False
