from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        count = 0
        for r in range(R-2):
            for c in range(C-2):
                r1c1 = grid[r][c]
                r1c2 = grid[r][c+1]
                r1c3 = grid[r][c+2]
                r2c1 = grid[r+1][c]
                r2c2 = grid[r+1][c+1]
                r2c3 = grid[r+1][c+2]
                r3c1 = grid[r+2][c]
                r3c2 = grid[r+2][c+1]
                r3c3 = grid[r+2][c+2]

                result = sorted([r1c1, r1c2, r1c3, r2c1, r2c2,
                                 r2c3, r3c1, r3c2, r3c3]) == list(range(1, 10))

                result &= (r1c1 + r1c2 + r1c3 == 15)
                result &= (r2c1 + r2c2 + r2c3 == 15)
                result &= (r2c1 + r2c2 + r2c3 == 15)
                result &= (r1c1 + r2c1 + r3c1 == 15)
                result &= (r1c2 + r2c2 + r3c2 == 15)
                result &= (r1c3 + r2c3 + r3c3 == 15)
                result &= (r1c1 + r2c2 + r3c3 == 15)
                result &= (r1c3 + r2c2 + r3c1 == 15)

                count += 1 if result else 0
        return count


if __name__ == "__main__":
    s = Solution()
    result = s.numMagicSquaresInside(
        [[4, 7, 8], [9, 5, 1], [2, 3, 6]])
    print(result)
