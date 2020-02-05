from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or (not matrix[0]):
            return False
        # first search rows
        row_ind = self.search_row(matrix, target)

        row = matrix[row_ind]

        # second search columns
        res = self.search_col(row, target)

        return res

    def search_row(self, matrix, target):
        low = 0; high = len(matrix) - 1
        while low + 1 < high:
            median = int((low + high) / 2)
            temp = matrix[median][0]
            if temp == target:
                return median
            elif temp > target:
                high = median - 1
            else:
                low = median
        if low == high:
            return low
        else:
            return high if matrix[high][0] <= target else low
    
    def search_col(self, row, target):
        low = 0; high = len(row) - 1
        while low + 1 < high:
            median = int((low + high) / 2)
            temp = row[median]
            if temp == target:
                return True
            elif temp < target:
                low = median + 1
            else:
                high = median - 1
        if target == row[low] or target == row[high]:
            return True
        else:
            return False
