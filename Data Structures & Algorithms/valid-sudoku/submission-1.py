class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = len(board)
        row = len(board[0])
        for i in range(col) :
            dup = []
            for j in range(row) :
                if board[j][i] in dup :
                    return False
                if board[j][i] == "." :
                    continue
                dup.append(board[j][i])
        
        dup = []
        for i in range(row) :
            dup = []
            for j in range(col) :
                if board[i][j] in dup :
                    return False
                if board[i][j] == "." :
                    continue
                dup.append(board[i][j])
        
        dup = []
        i, j = 0, 0
        while i < col :
            while j < row :
                dup = []
                for x in range(i, i+3) :
                    if x >= 9 : break
                    for y in range(j, j+3) :
                        if y >= 9 : break
                        if board[x][y] in dup :
                            return False
                        if board[x][y] == "." :
                            continue
                        dup.append(board[x][y])
                j += 3
            i += 3
        
        return True
