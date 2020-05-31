from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)


if __name__ == "__main__":
    s = Solution()
    result = s.maxProduct([3, 4, 5, 2])
    print(result)
