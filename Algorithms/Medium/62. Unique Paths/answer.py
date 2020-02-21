from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i + j in [0, 1]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


if __name__ == "__main__":
    s = Solution()
    result = s.uniquePaths(7, 3)
    print(result)
