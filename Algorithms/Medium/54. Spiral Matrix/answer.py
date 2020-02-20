from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for c in range(c1, c2+1):
                res.append(matrix[r1][c])
            for r in range(r1+1, r2+1):
                res.append(matrix[r][c2])
            if r1 < r2 and c1 < c2:
                for c in range(c2-1, c1, -1):
                    res.append(matrix[r2][c])
                for r in range(r2, r1, -1):
                    res.append(matrix[r][c1])
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.spiralOrder([
        [1, 2, 3, 4, 1],
        [5, 6, 7, 8, 2],
        [9, 10, 11, 12, 3]
    ])
    print(result)
