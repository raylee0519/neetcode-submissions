class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combination = []
        result = []
        def dfs(index, total) :
            if total == target :
                result.append(combination[:])
                return 

            if total > target :
                return

            for i in range(index, len(nums)) :
                combination.append(nums[i])
                
                dfs(i, total + nums[i])

                combination.pop()

        dfs(0,0)
        return result
        