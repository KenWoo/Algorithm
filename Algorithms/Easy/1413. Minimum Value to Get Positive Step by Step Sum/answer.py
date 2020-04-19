from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        N = len(nums)
        sums = [0] * (N + 1)
        for i in range(N):
            sums[i+1] = sums[i] + nums[i]
        print(sums)
        mi = min(sums[1:])
        return abs(mi) + 1 if mi <= 0 else 1


if __name__ == "__main__":
    s = Solution()
    result = s.minStartValue([2, 3, 5, -5, -1])
    print(result)
