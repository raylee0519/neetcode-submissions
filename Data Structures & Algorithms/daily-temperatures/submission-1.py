class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        result = [0] * len(temp)
        stack = []

        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

        return result