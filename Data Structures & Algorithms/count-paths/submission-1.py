class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            result[i][0] = 1

        for j in range(n):
            result[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = result[i - 1][j] + result[i][j - 1]

        return result[m - 1][n - 1]