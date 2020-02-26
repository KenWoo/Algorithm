from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        N = len(nums)
        l, r = 0, N - 1
        if N == 1 or nums[r] > nums[0]:
            return nums[0]
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1


if __name__ == "__main__":
    s = Solution()
    result = s.findMin([4, 5, 6, 7, 0, 1, 2])
    print(result)
