from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        lastPosition = N - 1
        for i in range(N-1, -1, -1):
            if i + nums[i] >= lastPosition:
                lastPosition = i
        return lastPosition == 0


if __name__ == "__main__":
    s = Solution()
    result = s.canJump([3, 2, 1, 0, 4])
    print(result)
