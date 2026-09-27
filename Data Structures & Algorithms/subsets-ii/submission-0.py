class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        subset = []

        def dfs(index):
            result.append(subset[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()

        dfs(0)
        return result