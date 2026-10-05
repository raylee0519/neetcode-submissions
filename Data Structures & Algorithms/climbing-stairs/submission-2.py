class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        # recursive
        def dfs(n) :
            if n <= 0 : return 0
            return dfs(n-1) + dfs(n-2)
        return dfs(n)
        '''
        memo = {}

        def dfs(n):
            if n < 0:
                return 0
            if n == 0:
                return 1

            if n in memo:
                return memo[n]

            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]

        return dfs(n)