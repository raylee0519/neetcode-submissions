class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        # 행 검사
        for i in range(rows):
            check = set()

            for j in range(cols):
                value = board[i][j]

                if value == ".":
                    continue

                if value in check:
                    return False

                check.add(value)

        # 열 검사
        for j in range(cols):
            check = set()

            for i in range(rows):
                value = board[i][j]

                if value == ".":
                    continue

                if value in check:
                    return False

                check.add(value)

        # 3 x 3 박스 검사
        for row_start in range(0, rows, 3):
            for col_start in range(0, cols, 3):
                check = set()

                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        value = board[i][j]

                        if value == ".":
                            continue

                        if value in check:
                            return False

                        check.add(value)

        return True