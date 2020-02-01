from typing import List


class Solution:
    def twoSum(self, nums, target):
        # Time Limit Exceeded
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            else:
                dict[nums[i]] = i


if __name__ == "__main__":
    s = Solution()
    result = s.twoSum([2, 7, 11, 15], 9)
    print(result)
