class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = [0] * len(nums)
        def robbery(index) :
            if index < 0 :
                return 0
            if memo[index] != 0 :
                return memo[index]
            memo[index] = max(robbery(index - 2) + nums[index], robbery(index - 1))
            return memo[index]
        return robbery(len(nums) - 1)