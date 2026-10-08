class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        memo = [-1] * length

        def robbery(n):
            if n >= length:
                return 0

            if memo[n] != -1:
                return memo[n]

            memo[n] = max(
                nums[n] + robbery(n + 2),  # 현재 집 털기
                robbery(n + 1)             # 현재 집 안 털기
            )

            return memo[n]

        return robbery(0)