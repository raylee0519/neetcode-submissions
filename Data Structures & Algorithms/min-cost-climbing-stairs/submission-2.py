class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def stairs(index):
            if index >= len(cost):
                return 0

            if memo[index] != -1:
                return memo[index]

            memo[index] = cost[index] + min(
                stairs(index + 1),
                stairs(index + 2)
            )

            return memo[index]

        return min(stairs(0), stairs(1))