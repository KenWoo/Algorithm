from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
        res = 0
        for i in range(1, row+1):
            for j in range(1, col+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                res += dp[i][j]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.countSquares([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ])
    print(result)
