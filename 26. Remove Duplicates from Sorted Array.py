from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            slow = 0; quick = 1
            while quick < len(nums):
                if nums[quick] != nums[slow]:
                    slow += 1
                    nums[slow] = nums[quick]
                quick +=1
            return slow + 1
