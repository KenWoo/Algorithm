from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        res = float('inf')
        for i in range(4):
            res = min(res, nums[-i-1] - nums[3-i])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.minDifference([6, 6, 0, 1, 1, 4, 6])
    print(result)
