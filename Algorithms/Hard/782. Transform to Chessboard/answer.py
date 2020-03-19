from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        N = len(board)
        rowSum = colSum = rowSwap = colSwap = 0
        for i in range(N):
            for j in range(N):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1
        for i in range(N):
            rowSum += board[0][i]
            colSum += board[i][0]
            rowSwap += board[i][0] == i % 2
            colSwap += board[0][i] == i % 2
        if N//2 > rowSum or rowSum > (N+1)//2:
            return -1
        if N//2 > colSum or colSum > (N+1)//2:
            return -1
        if N % 2:
            if rowSwap % 2:
                rowSwap = N - rowSwap
            if colSwap % 2:
                colSwap = N - colSwap
        else:
            rowSwap = min(N-rowSwap, rowSwap)
            colSwap = min(N-colSwap, colSwap)
        return (rowSwap + colSwap) // 2


if __name__ == "__main__":
    s = Solution()
    result = s.movesToChessboard(
        [[0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0]])
    print(result)
