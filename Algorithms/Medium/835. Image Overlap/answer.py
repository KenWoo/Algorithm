from typing import List
import collections


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        VA = [(x, y) for x in range(N) for y in range(N) if A[x][y]]
        VB = [(x, y) for x in range(N) for y in range(N) if B[x][y]]
        d = collections.Counter([(x1-x2, y1-y2)
                                 for (x1, y1) in VA for (x2, y2) in VB])
        return max(d.values() or [0])


if __name__ == "__main__":
    s = Solution()
    result = s.largestOverlap([[1, 1, 0],
                               [0, 1, 0],
                               [0, 1, 0]], [[0, 0, 0],
                                            [0, 1, 1],
                                            [0, 0, 1]])
    print(result)
