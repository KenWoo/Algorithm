from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1:
            return False
        tot = sum(nums)
        if tot % 2 != 0:
            return False
        tar = tot // 2
        dp = [[0] * (tar+1) for _ in range(N+1)]
        for i in range(1, N + 1):
            for j in range(1, tar + 1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]] + nums[i-1])
            if dp[i][j] == tar:
                return True
        return False
        
if __name__ == "__main__":
    s = Solution()
    result = s.canPartition( 
[1,2,3,4,5,6,7])
    print(result)