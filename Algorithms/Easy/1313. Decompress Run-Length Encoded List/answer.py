from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums) // 2):
            res.extend(nums[2*i] * [nums[2*i+1]])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.decompressRLElist([1, 2])
    print(result)
