class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        subset = []
        def dfs(opened, closed) :
            if opened == closed == n :
                result.append("".join(subset))
            if opened < n :
                subset.append("(")
                dfs(opened + 1, closed)
                subset.pop()
            if closed < opened :
                subset.append(")")
                dfs(opened, closed + 1)
                subset.pop()
        dfs(0, 0)
        return result