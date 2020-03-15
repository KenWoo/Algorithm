from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        Row = len(matrix)
        Col = len(matrix[0])
        r_set = set()
        for i in range(Row):
            r_set.add(min(matrix[i]))
        c_set = set()
        for j in range(Col):
            ma = matrix[0][j]
            for i in range(1, Row):
                ma = max(ma, matrix[i][j])
            c_set.add(ma)
        return list(r_set & c_set)


if __name__ == "__main__":
    s = Solution()
    result = s.luckyNumbers([[7, 8], [1, 2]])
    print(result)
