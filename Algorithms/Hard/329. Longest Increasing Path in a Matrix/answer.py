from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)]

        def dfs(x, y):
            val = matrix[x][y]
            if not dp[x][y]:
                dp[x][y] = 1 + max(
                    dfs(x - 1, y) if x and val < matrix[x - 1][y] else 0,
                    dfs(x, y - 1) if y and val < matrix[x][y - 1] else 0,
                    dfs(x + 1, y) if x < M-1 and val < matrix[x + 1][y] else 0,
                    dfs(x, y + 1) if y < N-1 and val < matrix[x][y + 1] else 0
                )
            return dp[x][y]

        res = 0
        for i in range(M):
            for j in range(N):
                res = max(res, dfs(i, j))
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.longestIncreasingPath([[1, 2]])
    print(result)
