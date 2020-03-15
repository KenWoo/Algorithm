from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = point = ma = 0
        for i in range(len(nums)-1):
            ma = max(ma, i + nums[i])
            if i == point:
                point = ma
                step += 1
        return step


if __name__ == "__main__":
    s = Solution()
    result = s.jump([2, 3, 1, 1, 4])
    print(result)
