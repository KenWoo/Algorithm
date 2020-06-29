from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        i = s = res = 0
        for j in range(N):
            s += nums[j]
            while i < j and s < j - i:
                s -= nums[i]
                i += 1
            res = max(res, j - i)
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.longestSubarray([0,1,1,1,0,1,1,0,1])
    print(result)