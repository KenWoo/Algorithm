from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row = [0] * n
        col = [0] * m
        for index in indices:
            row[index[0]] += 1
            col[index[1]] += 1
        count = 0
        for i in row:
            for j in col:
                if (i+j) % 2 != 0:
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    result = s.oddCells(2, 3, [[0, 1], [1, 1]])
    print(result)
