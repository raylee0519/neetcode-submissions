class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(n + 1) :
            dp[1][i] = 1
        for j in range(m + 1) :
            dp[j][1] = 1
        for i in range(2, m + 1) :
            for j in range(2, n + 1) :
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]