from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        N = len(nums)
        left = 0
        right = N - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        start = -1 if nums[left] != target else left
        left = 0
        right = N - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        end = -1 if nums[right] != target else right
        return [start, end]


if __name__ == "__main__":
    s = Solution()
    result = s.searchRange([2, 2, 3], 3)
    print(result)
