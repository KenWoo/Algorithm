from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        r1, r2 = 0, n - 1
        c1, c2 = 0, n - 1
        index = 1
        while index <= n**2:
            for c in range(c1, c2+1):
                res[r1][c] = index
                index += 1
            for r in range(r1+1, r2+1):
                res[r][c2] = index
                index += 1
            for c in range(c2-1, c1-1, -1):
                res[r2][c] = index
                index += 1
            for r in range(r2-1, r1, -1):
                res[r][c1] = index
                index += 1
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.generateMatrix(5)
    print(result)
