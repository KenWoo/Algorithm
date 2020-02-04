from typing import List
import math


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        r = len(M)
        c = len(M[0])
        mm = []
        for i in range(r):
            m = []
            for j in range(c):
                count = 0
                v = 0
                for x in [i-1, i, i+1]:
                    for y in [j-1, j, j+1]:
                        if x >= 0 and x <= r-1 and y >= 0 and y <= c-1:
                            count += 1
                            v += M[x][y]
                m.append(int(v / count))
            mm.append(m)

        return mm


if __name__ == "__main__":
    s = Solution()
    result = s.imageSmoother(
        [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]])
    print(result)
