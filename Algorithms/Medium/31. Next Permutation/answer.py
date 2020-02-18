from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        N = len(nums)
        pivot = N - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot+1]:
            pivot -= 1
        if pivot >= 0:
            point = N - 1
            while point > pivot and nums[point] <= nums[pivot]:
                point -= 1
            nums[pivot], nums[point] = nums[point], nums[pivot]
        start = pivot + 1
        end = N - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 5, 1]
    s.nextPermutation(nums)
    print(nums)
