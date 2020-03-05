from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l = res = 0
        prod = 1
        for r, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[l]
                l += 1
            res += r - l + 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
    print(result)
