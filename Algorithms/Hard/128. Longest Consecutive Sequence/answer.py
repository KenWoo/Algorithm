from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            if n not in s:
                continue
            pre, next = n - 1, n + 1
            while pre in s:
                s.remove(pre)
                pre -= 1
            while next in s:
                s.remove(next)
                next += 1
            res = max(res, next-pre-1)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.longestConsecutive([100, 4, 200, 1, 3, 2])
    print(result)
