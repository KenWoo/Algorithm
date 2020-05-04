from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        l = 0
        mi = []
        ma = []
        N = len(nums)
        for r in range(N):
            while mi and nums[mi[-1]] >= nums[r]:
                mi.pop()
            mi.append(r)
            while ma and nums[ma[-1]] <= nums[r]:
                ma.pop()
            ma.append(r)
            while l < r and nums[ma[0]] - nums[mi[0]] > limit:
                if l == mi[0]:
                    mi.pop(0)
                if l == ma[0]:
                    ma.pop(0)
                l += 1
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.longestSubarray([8, 2, 4, 7], 4)
    print(result)
