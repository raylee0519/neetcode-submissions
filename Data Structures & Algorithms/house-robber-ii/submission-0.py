class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robbery(start, end):
            memo = [-1] * len(nums)

            def dfs(n):
                if n > end:
                    return 0

                if memo[n] != -1:
                    return memo[n]

                memo[n] = max(
                    nums[n] + dfs(n + 2),
                    dfs(n + 1)
                )

                return memo[n]

            return dfs(start)

        return max(
            robbery(0, len(nums) - 2),  # 마지막 집 제외
            robbery(1, len(nums) - 1)   # 첫 집 제외
        )