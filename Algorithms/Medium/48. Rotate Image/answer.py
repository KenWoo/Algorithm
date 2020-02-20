from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        for i in range(N):
            for j in range(i+1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(N):
            for j in range(N // 2):
                matrix[i][j], matrix[i][N-j-1] = matrix[i][N-j-1], matrix[i][j]


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    s.rotate(matrix)
    print(matrix)
