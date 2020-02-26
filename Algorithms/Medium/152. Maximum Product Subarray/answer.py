from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return nums
        res = mi = ma = nums[0]
        for i in range(1, len(nums)):
            ma, mi = max(nums[i], nums[i]*ma, nums[i] *
                         mi), min(nums[i], nums[i]*ma, nums[i]*mi)
            res = max(res, ma)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maxProduct([2, 3, -2, 4])
    print(result)
