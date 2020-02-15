from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                new_col = (col + k) % n
                new_row = (row + (col + k) // n) % m
                res[new_row][new_col] = grid[row][col]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9)
    print(result)
