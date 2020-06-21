from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(n+1):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
                j += 1
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    result = s.numSquares(12)
    print(result)
