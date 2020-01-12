class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            cur1 = nums1[m - 1]
            cur2 = nums2[n - 1]
            if cur1 > cur2:
                nums1[m + n - 1] = cur1
                m -= 1
            else:
                nums1[m + n - 1] = cur2
                n -= 1
        nums1[:n] = nums2[:n]
