class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combination = []
        result = []

        def dfs():
            if len(combination) == len(nums):
                result.append(combination[:])
                return

            for i in range(len(nums)):
                if nums[i] in combination:
                    continue

                combination.append(nums[i])
                dfs()
                combination.pop()

        dfs()
        return result