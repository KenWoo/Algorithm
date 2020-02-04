from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        index = count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                index = i

            if count > 1:
                return False

        return count == 0 or index == 0 or index == len(nums) - 2 or nums[index - 1] <= nums[index + 1] or nums[index] <= nums[index + 2]


if __name__ == "__main__":
    s = Solution()
    result = s.checkPossibility([-1, 42, 2, 11, 2])
    print(result)
