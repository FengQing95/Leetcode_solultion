class Solution:
    def removeElement(self, nums, val: int):
        if len(nums) == 1:
            return 0 if nums[0] == val else 1

        left = 0; right = len(nums) - 1
        count = 0
        while left <= right:
            if nums[right] == val:
                right -= 1
                count += 1
                continue
            if nums[left] != val:
                left += 1
                continue
            
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            count += 1
        return len(nums) - count
