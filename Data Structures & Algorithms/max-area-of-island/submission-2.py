class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_area = 0

        def dfs(r,c) :
            if r < 0 or r >= row or c < 0 or c>= col or grid[r][c] == 0:
                return 0

            count = 1
            grid[r][c] = 0
            count += dfs(r + 1, c)
            count += dfs(r, c + 1)
            count += dfs(r - 1, c)
            count += dfs(r, c - 1)

            return count

        for i in range(row) :
            for j in range(col) :
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    max_area = max(max_area, area)
        return max_area