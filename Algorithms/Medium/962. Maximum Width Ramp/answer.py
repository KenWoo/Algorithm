from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        res = 0
        N = len(A)
        sortedA = sorted(range(N), key=A.__getitem__)
        m = float('inf')
        for i in sortedA:
            res = max(res, i-m)
            m = min(m, i)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1])
    print(result)
