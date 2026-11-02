class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if visited[r][c]:
                return

            if board[r][c] != "O":
                return

            visited[r][c] = True

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 위 / 아래 edge
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)

            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        # 왼쪽 / 오른쪽 edge
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        # edge와 연결되지 않은 O만 X로 변경
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and not visited[r][c]:
                    board[r][c] = "X"