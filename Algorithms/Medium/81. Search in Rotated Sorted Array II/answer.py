from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        l, r = 0, N-1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return True
            if nums[l] < nums[mid]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
        return False


if __name__ == "__main__":
    s = Solution()
    result = s.search([1, 3, 1, 1, 1], 3)
    print(result)
