from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        Row = len(mat)
        Col = len(mat[0])
        presum = [[0 for _ in range(Col+1)] for _ in range(Row+1)]
        for i in range(1, Row+1):
            for j in range(1, Col+1):
                presum[i][j] = presum[i][j-1] + presum[i-1][j] - \
                    presum[i-1][j-1] + mat[i-1][j-1]

        k = min(Row, Col)
        while k > 0:
            for i in range(Row-k+1):
                for j in range(Col-k+1):
                    if presum[i+k][j+k] + presum[i][j] - presum[i+k][j] - presum[i][j+k] <= threshold:
                        return k
            k -= 1
        return 0


if __name__ == "__main__":
    s = Solution()
    result = s.maxSideLength(
        [[18, 70], [61, 1], [25, 85], [14, 40], [11, 96], [97, 96], [63, 45]], 40184)
    print(result)
