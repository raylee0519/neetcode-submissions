class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combination = []
        result = []
        visited = [False] * len(nums)

        def dfs() :
            if len(combination) == len(nums) :
                result.append(combination[:])
                return
            for i in range(len(nums)) :
                if visited[i] == True : continue
                combination.append(nums[i])
                visited[i] = True
                dfs()
                combination.pop()
                visited[i] = False
                
        dfs()
        return result