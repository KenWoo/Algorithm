from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        res = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    l, r, t, d = j-1, j+1, i-1, i+1
                    if l < 0 or grid[i][l] == 0:
                        res += 1
                    if r >= C or grid[i][r] == 0:
                        res += 1
                    if t < 0 or grid[t][j] == 0:
                        res += 1
                    if d >= R or grid[d][j] == 0:
                        res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.islandPerimeter([[0, 1, 0, 0],
                                [1, 1, 1, 0],
                                [0, 1, 0, 0],
                                [1, 1, 0, 0]]
                               )
    print(result)
