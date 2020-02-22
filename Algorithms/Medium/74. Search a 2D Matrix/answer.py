from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        row = l - 1
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


if __name__ == "__main__":
    s = Solution()
    result = s.searchMatrix([
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 12)
    print(result)
