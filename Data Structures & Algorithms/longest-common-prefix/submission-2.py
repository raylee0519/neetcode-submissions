class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float("inf")
        answer = ""
        for i in strs:
            length = min(len(i), length)

        j = 0
        while j < length:
            for k in range(1, len(strs)):
                if strs[k][j] != strs[0][j]:
                    return answer
            answer += strs[0][j]
            j += 1
        return answer