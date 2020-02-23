from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res += [x + [n] for x in res]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.subsets([1, 2, 3])
    print(result)
