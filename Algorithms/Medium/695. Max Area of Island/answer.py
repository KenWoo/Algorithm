from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        Row, Col = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= Row or c < 0 or c >= Col or grid[r][c] in (0, 2):
                return 0
            count = 1
            grid[r][c] = 2
            count += dfs(r-1, c)
            count += dfs(r+1, c)
            count += dfs(r, c-1)
            count += dfs(r, c+1)
            return count

        for i in range(Row):
            for j in range(Col):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
    print(result)
