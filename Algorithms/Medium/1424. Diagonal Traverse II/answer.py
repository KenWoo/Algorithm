from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dict = {}
        ma = 0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                k = i + j
                dict.setdefault(k, [])
                dict[k].append(nums[i][j])
                ma = max(ma, i+j)
        res = []
        for i in range(ma+1):
            for j in range(len(dict[i])-1, -1, -1):
                res.append(dict[i][j])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findDiagonalOrder(
        [[14, 12, 19, 16, 9], [13, 14, 15, 8, 11], [11, 13, 1]])
    print(result)
