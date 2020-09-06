from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        res = 0
        for i in range(N):
            res += mat[i][i]
            res += mat[i][N-i-1]
        if N % 2 != 0:
            res -= mat[N//2][N//2]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.diagonalSum([[1, 1, 1, 1],
                            [1, 1, 1, 1],
                            [1, 1, 1, 1],
                            [1, 1, 1, 1]])
    print(result)
