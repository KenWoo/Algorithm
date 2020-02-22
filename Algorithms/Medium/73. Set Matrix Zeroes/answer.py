from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        s = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if (i, j) not in s:
                        for c in range(n):
                            if matrix[i][c] != 0:
                                matrix[i][c] = 0
                                s.add((i, c))
                        for r in range(m):
                            if matrix[r][j] != 0:
                                matrix[r][j] = 0
                                s.add((r, j))
        return matrix


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    s.setZeroes(matrix)
    print(matrix)
