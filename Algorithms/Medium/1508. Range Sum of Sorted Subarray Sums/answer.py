from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                res.append(s)
        res.sort()
        return sum(res[left-1:right])


if __name__ == "__main__":
    s = Solution()
    result = s.rangeSum([1, 2, 3, 4], 4, 3, 4)
    print(result)
