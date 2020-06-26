from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        dp = [0] * N
        dp[0] = 1
        res = 1
        for i in range(1, N):
            val = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    val = max(val, dp[j])
            dp[i] = val + 1
            res = max(res, dp[i])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print(result)
