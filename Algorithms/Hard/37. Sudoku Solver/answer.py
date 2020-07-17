from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(x, y):
            tmp = board[x][y]
            board[x][y] = '.'
            for i in range(9):
                if board[i][y] == tmp:
                    return False
            for i in range(9):
                if board[x][i] == tmp:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[int(x/3)*3+i][int(y/3)*3+j] == tmp:
                        return False
            board[x][y] = tmp
            return True
            
        def dfs():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j] = k
                            if isValid(i, j) and dfs():
                                return True
                            board[i][j] = '.'
                        return False
            return True
        dfs()

if __name__ == "__main__":
    pass