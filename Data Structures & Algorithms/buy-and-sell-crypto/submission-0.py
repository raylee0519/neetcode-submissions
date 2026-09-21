class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        lowest = float('inf')
        for i in prices :
            lowest = min(lowest, i)
            result = max(i - lowest, result)
        return result