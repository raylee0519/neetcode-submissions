class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def robbery(n) :
            if n < 0 :
                return 0
            if memo[n] != -1 :
                return memo[n]
            memo[n] = max(robbery(n-1), robbery(n-2) + nums[n])
            return memo[n]
        return robbery(len(nums)-1)