from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count_row = [0] * row
        count_col = [0] * col
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count_row[i] += 1
                    count_col[j] += 1
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (count_row[i] > 1 or count_col[j] > 1):
                    res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.countServers([[1, 0], [1, 1]])
    print(result)
