class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        # 길이 1은 항상 palindrome
        for i in range(n):
            dp[i][i] = True

        # 길이 2부터 확인
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right]:
                    if length == 2:
                        dp[left][right] = True
                    else:
                        dp[left][right] = dp[left + 1][right - 1]

                if dp[left][right] and length > max_len:
                    start = left
                    max_len = length

        return s[start:start + max_len]