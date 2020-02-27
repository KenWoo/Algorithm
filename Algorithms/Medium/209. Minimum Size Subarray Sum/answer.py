from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res, l, sum, N = float('inf'), 0, 0, len(nums)
        for i in range(N):
            sum += nums[i]
            while sum >= s:
                res = min(res, i+1-l)
                sum -= nums[l]
                l += 1
        return 0 if res == float('inf') else res


if __name__ == "__main__":
    s = Solution()
    result = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(result)
