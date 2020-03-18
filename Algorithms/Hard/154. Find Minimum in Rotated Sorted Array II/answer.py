from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        left, right = 0, N-1
        while left < right and nums[left] >= nums[right]:
            mid = left + (right-left) // 2
            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] == nums[left]:
                left += 1
            else:
                left = mid + 1
        return nums[left]


if __name__ == "__main__":
    s = Solution()
    result = s.findMin([2, 2, 2, 0, 1])
    print(result)
