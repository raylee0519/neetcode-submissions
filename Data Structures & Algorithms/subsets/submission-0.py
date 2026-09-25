class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(index):
            result.append(subset[:])

            for i in range(index, len(nums)):
                subset.append(nums[i])   # 선택
                dfs(i + 1)               # 다음 숫자부터 탐색
                subset.pop()             # 선택 취소

        dfs(0)
        return result