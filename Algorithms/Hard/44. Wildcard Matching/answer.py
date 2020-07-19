from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)
        dp = [[False for j in range(N+1)] for i in range(M+1)]
        dp[0][0] = True
        for j in range(1, N+1):
            dp[0][j] = p[j-1] == '*' and dp[0][j-1]
        for i in range(1, M+1):
            for j in range(1, N+1):
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[M][N]


if __name__ == "__main__":
    pass
