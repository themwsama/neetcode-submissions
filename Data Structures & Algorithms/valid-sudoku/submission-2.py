class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = {}
            col_set = {}
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_set: return False
                    row_set[board[i][j]] = True
                if board[j][i] != ".":
                    if board[j][i] in col_set: return False
                    col_set[board[j][i]] = True

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                duplicate={}
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        if (board[i][j] in duplicate) and (board[i][j] != "."):
                            return False
                        else:
                            duplicate[board[i][j]] = True

        return True