class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]
        def find(i, j) :
            if i == m - 1 and j == n - 1:
                return 1
            if i > m - 1 or j > n - 1 :
                return 0
            if memo[i][j] != 0 :
                return memo[i][j]
            memo[i][j] = find(i + 1, j) + find(i, j + 1)
            return memo[i][j]
        return find(0, 0)