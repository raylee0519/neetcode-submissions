class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)

        def change(amount):
            if amount == 0:
                return 0

            if amount < 0:
                return float('inf')

            if memo[amount] != -1:
                return memo[amount]

            result = float('inf')

            for coin in coins:
                result = min(
                    result,
                    change(amount - coin) + 1
                )

            memo[amount] = result
            return result

        answer = change(amount)

        if answer == float('inf'):
            return -1

        return answer