from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dict = {}
        for r, row in enumerate(matrix):
            for c, col in enumerate(row):
                if r - c not in dict:
                    dict[r-c] = col
                elif dict[r-c] != col:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
    print(result)
