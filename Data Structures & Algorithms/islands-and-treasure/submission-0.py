from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        # 1. 모든 treasure(0)를 먼저 queue에 넣음
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # 2. 모든 treasure에서 동시에 BFS
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols
                ):
                    continue

                # INF인 빈 공간만 처음 방문
                if grid[nr][nc] != 2147483647:
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))