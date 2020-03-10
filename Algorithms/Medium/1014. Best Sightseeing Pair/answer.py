from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        cur = res = 0
        for a in A:
            res = max(res, cur + a)
            cur = max(cur, a) - 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maxScoreSightseeingPair([8, 1, 5, 2, 6])
    print(result)
