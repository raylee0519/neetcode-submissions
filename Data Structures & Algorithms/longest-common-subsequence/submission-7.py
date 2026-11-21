class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        def lcs(t1, t2):
            if t1 == 0 or t2 == 0:
                return 0

            if dp[t1][t2] != -1:
                return dp[t1][t2]

            if text1[t1 - 1] == text2[t2 - 1]:
                dp[t1][t2] = lcs(t1 - 1, t2 - 1) + 1
            else:
                dp[t1][t2] = max(
                    lcs(t1 - 1, t2),
                    lcs(t1, t2 - 1)
                )

            return dp[t1][t2]

        return lcs(len(text1), len(text2))