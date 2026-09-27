class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combination = []
        result = []

        def dfs(index, total) :
            if total == target :
                result.append(combination[:])
                return
            if total > target :
                return
            for i in range(index, len(candidates)) :
                if i > index and candidates[i] == candidates[i - 1] : continue
                combination.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                combination.pop()
        dfs(0, 0)
        return result