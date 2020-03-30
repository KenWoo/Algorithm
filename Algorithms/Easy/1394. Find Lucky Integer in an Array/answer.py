from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict = {}
        for a in arr:
            dict.setdefault(a, 0)
            dict[a] += 1
        res = -1
        for k, v in dict.items():
            if k == v:
                res = max(res, k)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findLucky([1, 2, 2, 3, 3, 3])
    print(result)
