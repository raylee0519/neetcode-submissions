class Solution:
    def partition(self, s: str) -> List[List[str]]:
        subset = []
        result = []

        def dfs(index):
            if index == len(s):
                result.append(subset[:])
                return

            for i in range(index, len(s)):
                part = s[index:i + 1]

                if part == part[::-1]:
                    subset.append(part)
                    dfs(i + 1)
                    subset.pop()

        dfs(0)
        return result