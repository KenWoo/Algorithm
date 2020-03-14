from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        res = 0
        for r in range(N):
            if grid[r][0] >= 0 and grid[r][M-1] >= 0:
                continue
            if grid[r][0] < 0:
                res += M
            else:
                k = 0
                while k < N:
                    if grid[r][k] < 0:
                        break
                    k += 1
                res += M - k
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.countNegatives(
        [[7, -3]])
    print(result)
