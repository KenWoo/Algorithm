from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = len(nums)
        max_num = nums[0]
        index = 0
        for i in range(1, m):
            if nums[i] > max_num:
                index = i
                max_num = nums[i]

        for i in range(m):
            if i != index and nums[i] * 2 > max_num:
                return -1
        return index


if __name__ == "__main__":
    s = Solution()
    result = s.dominantIndex([3, 6, 1, 0])
    print(result)
