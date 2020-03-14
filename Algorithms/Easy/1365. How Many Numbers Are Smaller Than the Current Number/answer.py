from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        dict = {}
        for i, n in enumerate(sorted_nums):
            if n not in dict:
                dict[n] = i
        N = len(nums)
        res = [0] * N
        for i, n in enumerate(nums):
            res[i] = dict[n]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.smallerNumbersThanCurrent([7, 7, 7, 7])
    print(result)
