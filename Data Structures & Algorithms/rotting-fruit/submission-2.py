class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        q = deque()
        row = len(grid)
        col = len(grid[0])
        count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    count += 1

        minute = 0

        while q and count > 0:
            for _ in range(len(q)):
                i, j = q.popleft()

                directions = [(1,0), (0,1), (-1,0), (0,-1)]

                for di, dj in directions:
                    ni = i + di
                    nj = j + dj

                    if (
                        0 <= ni < row and
                        0 <= nj < col and
                        grid[ni][nj] == 1
                    ):
                        grid[ni][nj] = 2
                        count -= 1
                        q.append((ni, nj))

            minute += 1

        if count > 0:
            return -1

        return minute