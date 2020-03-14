from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while True:
            cur1 = numbers[left]
            cur2 = numbers[right]
            if cur1 + cur2 > target:
                right -= 1
            elif cur1 + cur2 < target:
                left += 1
            else:
                break
        return [left+1, right+1]
