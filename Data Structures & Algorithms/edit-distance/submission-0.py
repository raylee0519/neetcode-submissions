class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        def edit(i, j) :
            if i == 0 :
                return j
            if j == 0 :
                return i
            if memo[i][j] != -1:
                return memo[i][j]

            if word1[i - 1] == word2[j - 1]:
                memo[i][j] = edit(i - 1, j - 1)

            else:
                memo[i][j] = 1 + min(
                    edit(i - 1, j),      # delete
                    edit(i, j - 1),      # insert
                    edit(i - 1, j - 1)   # replace
                )
            return memo[i][j]
        return edit(len(word1), len(word2))