from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        a, b = len(A), len(B)
        dp = [[0 for _ in range(b)] for _ in range(a)]
        for i in range(a):
            for j in range(b):
                if A[i] == B[j]:
                    dp[i][j] = max(dp[i][j], 1)
                    if i >= 1 and j >= 1:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
                else:
                    if i >= 1 and j >= 1:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-1])
                    if i >= 1:
                        dp[i][j] = max(dp[i][j], dp[i-1][j])
                    if j >= 1:
                        dp[i][j] = max(dp[i][j], dp[i][j-1])
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    A = [1, 4, 2]
    B = [1, 2, 4]
    result = s.maxUncrossedLines(A, B)
    print(result)
