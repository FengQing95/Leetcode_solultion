from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = {}
        for num in nums:
            if num in num2freq:
                num2freq[num] += 1
            else:
                num2freq[num] = 1
        
        freq2num = {}
        for num, freq in num2freq.items():
            if freq in freq2num:
                freq2num[freq].append(num)
            else:
                freq2num[freq] = [num]
        
        res = []
        for i in range(len(nums), 0, -1):
            if i in freq2num:
                res += freq2num[i]
            if len(res) >= k:
                break
        return res
