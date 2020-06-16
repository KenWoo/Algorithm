from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


if __name__ == "__main__":
    s = Solution()
    result = s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(result)
