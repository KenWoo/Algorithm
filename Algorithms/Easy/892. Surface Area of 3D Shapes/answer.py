from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res = 0
        N = len(grid)
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    res += grid[i][j] * 4 + 2
                if i:
                    res -= min(grid[i][j], grid[i-1][j]) * 2
                if j:
                    res -= min(grid[i][j], grid[i][j-1]) * 2
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.surfaceArea([[2]])
    print(result)
