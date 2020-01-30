class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        elif len(nums) == 3:
            return [] if sum(nums) != 0 else [nums]
        else:
            nums.append(float("-inf"))
            nums = sorted(nums)
            prev = 0
            res = []
            for cur in range(1, len(nums) - 2):
                if nums[cur] != nums[prev]:
                    rest = nums[cur + 1:]
                    target = 0 - nums[cur]
                    new_pairs = self.twoSum(rest, target)
                    for pair in new_pairs:
                        pair.append(nums[cur])
                        res.append(pair)
                prev = cur; cur += 1
            return res
                                  
    def twoSum(self, rest, target: int):
        res = []
        count = {}
        for num in rest:
            if num not in count:
                if target - num in count:
                    res.append([num, target - num])
                count[num] = 1
            else:
                if num == target / 2 and count[num] == 1:
                    res.append([num, num])
                count[num] += 1
        return res
