from typing import List

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        M, N = len(matrix), len(matrix[0])
        row, col = 0, N - 1
        while row < M and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
        
if __name__ == "__main__":
    s = Solution()
    result = s.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 19)
    print(result)