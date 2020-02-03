from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        start = end = 0
        s_flag = e_flag = False

        for i in range(n):
            if s_flag and e_flag:
                break
            if not s_flag and nums[i] != sorted_nums[i]:
                s_flag = True
                start = i
            if not e_flag and nums[n - i - 1] != sorted_nums[n - i - 1]:
                e_flag = True
                end = n - i - 1

        return end - start + 1 if end != 0 else end - start


if __name__ == "__main__":
    s = Solution()
    result = s.findUnsortedSubarray([1, 3, 2, 2, 2])
    print(result)
