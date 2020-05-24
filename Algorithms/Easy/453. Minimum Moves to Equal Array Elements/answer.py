from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mi = min(nums)
        res = 0
        for n in nums:
            res += n - mi
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.minMoves([1, 2, 3])
    print(result)
