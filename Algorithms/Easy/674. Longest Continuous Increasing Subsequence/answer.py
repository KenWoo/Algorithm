from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        start = end = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                end = i + 1
                count = max(count, end - start + 1)
            else:
                start = i + 1
        return count


if __name__ == "__main__":
    s = Solution()
    result = s.findLengthOfLCIS([6, 1, 2, 3, 5, 4, 7])
    print(result)
