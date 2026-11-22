class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        result = [[0] * col for _ in range(row)]
        result[0][0] = grid[0][0]
        for i in range(1, row) :
            result[i][0] = result[i-1][0] + grid[i][0]
        for j in range(1, col) :
            result[0][j] = result[0][j - 1] + grid[0][j]
        for i in range(1, row) :
            for j in range(1, col) :
                result[i][j] = min(result[i - 1][j], result[i][j-1]) + grid[i][j]
        return result[row - 1][col - 1]