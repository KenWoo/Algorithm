from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N-1):
            res += abs(nums[i+1] - nums[i])
        diff = 0
        mi, ma = float('inf'), float('-inf')
        for i in range(N-1):
            mi = min(mi, max(nums[i], nums[i+1]))
            ma = max(ma, min(nums[i], nums[i+1]))
        diff = max(diff, 2 * (ma - mi))
        for i in range(1, N-1):
            diff = max(diff, abs(nums[i+1] - nums[0]
                                 ) - abs(nums[i+1] - nums[i]))
        for i in range(1, N-1):
            diff = max(diff, abs(nums[i-1] - nums[N-1]
                                 ) - abs(nums[i-1] - nums[i]))
        return res + diff


if __name__ == "__main__":
    s = Solution()
    result = s.maxValueAfterReverse([2, 4, 9, 24, 2, 1, 10])
    print(result)
