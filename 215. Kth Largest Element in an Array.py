from typing import List
from random import sample

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums) -1
        self.quick_sort(nums, low, high)
        print(nums)
        return nums[-k]

    def quick_sort(self, nums, low, high):
        if low < high:
            p = self.partition(nums, low, high)
            self.quick_sort(nums, low, p - 1)
            self.quick_sort(nums, p + 1, high)
    
    def partition(self, nums, low, high):
        p = sample(range(low, high), 1)[0]
        nums[p], nums[high] = nums[high], nums[p]
        r = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= r:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1
