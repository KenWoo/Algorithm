from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while nums[i] > 0 and nums[i] <= N and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[tmp-1] = tmp
        for i in range(N):
            if nums[i] != i+1:
                return i+1
        return N+1


if __name__ == "__main__":
    s = Solution()
    result = s.firstMissingPositive([7, 8, 9, 11, 12])
    print(result)
