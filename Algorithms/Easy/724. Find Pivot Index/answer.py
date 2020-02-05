from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        m = len(nums)
        n_sum = sum(nums)
        l_sum = 0
        for i in range(m):
            if l_sum == n_sum - l_sum - nums[i]:
                return i
            l_sum += nums[i]
        return -1


if __name__ == "__main__":
    s = Solution()
    result = s.pivotIndex([1, 7, 3, 6, 5, 6])
    print(result)
