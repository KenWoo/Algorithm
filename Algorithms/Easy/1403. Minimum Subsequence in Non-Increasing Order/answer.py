from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        i, N = 0, len(nums)
        s = sum(nums)
        sum_arr = [0] * (N + 1)
        for i, n in enumerate(nums):
            sum_arr[i+1] = sum_arr[i] + n
            if sum_arr[i+1] > s - sum_arr[i+1]:
                return nums[0:i+1]


if __name__ == "__main__":
    s = Solution()
    result = s.minSubsequence([4, 3, 10, 9, 8])
    print(result)
