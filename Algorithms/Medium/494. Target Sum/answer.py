from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        N = len(nums)
        dp = [[0] * 2001 for _ in range(N)]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, N):
            for sum in range(-1000, 1001):
                if dp[i-1][sum+1000] > 0:
                    dp[i][sum+nums[i]+1000] += dp[i-1][sum+1000]
                    dp[i][sum-nums[i]+1000] += dp[i-1][sum+1000]
        return 0 if S > 1000 else dp[N-1][S+1000]

if __name__ == "__main__":
    s = Solution()
    result = s.findTargetSumWays([1, 1, 1, 1, 1], 3)
    print(result)