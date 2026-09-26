class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        
        def dfs(index) :
            result.append(subset[:])
            
            for i in range(index, len(nums)) :
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
                
        dfs(0)
        return result