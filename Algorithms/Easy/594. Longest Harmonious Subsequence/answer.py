from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict = {}
        for n in nums:
            dict.setdefault(n, 0)
            dict[n] += 1
        l = list(dict.keys())
        l.sort()
        res = 0
        for i in range(len(l)-1):
            if l[i+1] - l[i] == 1:
                res = max(res, dict[l[i]] + dict[l[i+1]])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findLHS([1, 3, 2, 2, 5, 2, 3, 7])
    print(result)
