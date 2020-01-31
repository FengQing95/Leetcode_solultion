from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        else:
            slow = 0; quick = 1
            count = 1
            while quick < n:
                if nums[quick] != nums[slow]:
                    slow += 1
                    nums[slow] = nums[quick]
                    count = 1
                else:
                    if count == 1:
                        slow += 1
                        nums[slow] = nums[quick]
                    count += 1
                quick += 1
            print(nums[:slow + 1])
            return slow + 1
