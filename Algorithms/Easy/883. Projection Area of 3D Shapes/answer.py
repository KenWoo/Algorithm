from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        res = 0
        for i in range(N):
            mrow = mcol = 0
            for j in range(N):
                if grid[i][j]:
                    res += 1
                mrow = max(mrow, grid[i][j])
                mcol = max(mcol, grid[j][i])
            res += mrow + mcol
        return res


if __name__ == "__main__":
    pass
