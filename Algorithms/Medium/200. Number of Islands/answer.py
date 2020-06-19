from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        M, N = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= M or y < 0 or y >= N or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res


if __name__ == "__main__":
    pass
