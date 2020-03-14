class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        res = [row] * m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    res[i][j] = 1
                    continue

                above = res[i-1][j]
                left = res[i][j-1]
                res[i][j] = left + above
        print(res)
        return res[-1][-1]
