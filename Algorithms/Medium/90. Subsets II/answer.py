from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        for n in nums:
            res += [[n] + x for x in res if [n] + x not in res]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.subsetsWithDup([4, 4, 4, 1, 4])
    print(result)
