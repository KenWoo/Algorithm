from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        grid = [[0] * 8 for _ in range(8)]
        for i, j in queens:
            grid[i][j] = 1
        r, c = king[0], king[1]
        res = []
        for i in range(c-1, -1, -1):
            if grid[r][i] == 1:
                res.append([r, i])
                break
        for i in range(c+1, 8):
            if grid[r][i] == 1:
                res.append([r, i])
                break
        for i in range(r-1, -1, -1):
            if grid[i][c] == 1:
                res.append([i, c])
                break
        for i in range(r+1, 8):
            if grid[i][c] == 1:
                res.append([i, c])
                break
        i, j = r, c
        while i >= 0 and j >= 0:
            if grid[i][j] == 1:
                res.append([i, j])
                break
            i -= 1
            j -= 1
        i, j = r, c
        while i >= 0 and j < 8:
            if grid[i][j] == 1:
                res.append([i, j])
                break
            i -= 1
            j += 1
        i, j = r, c
        while i < 8 and j >= 0:
            if grid[i][j] == 1:
                res.append([i, j])
                break
            i += 1
            j -= 1
        i, j = r, c
        while i < 8 and j < 8:
            if grid[i][j] == 1:
                res.append([i, j])
                break
            i += 1
            j += 1

        return res


if __name__ == "__main__":
    s = Solution()
    queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
    king = [0, 0]
    result = s.queensAttacktheKing(queens, king)
    print(result)
