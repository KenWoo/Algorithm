from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1),
                     (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                l_n = 0
                for n in neighbors:
                    r = row + n[0]
                    c = col + n[1]
                    if r >= 0 and r < rows and c >= 0 and c < cols and abs(board[r][c]) == 1:
                        l_n += 1
                if board[row][col] == 1 and (l_n < 2 or l_n > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and l_n == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0


if __name__ == "__main__":
    s = Solution()
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    s.gameOfLife(board)
    print(board)
