from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1, N):
            obstacleGrid[0][i] = int(
                obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1)
        for i in range(1, M):
            obstacleGrid[i][0] = int(
                obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
        for i in range(1, M):
            for j in range(1, N):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + \
                        obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[M-1][N-1]


if __name__ == "__main__":
    s = Solution()
    result = s.uniquePathsWithObstacles([[0, 0, 0],
                                         [0, 1, 0],
                                         [0, 0, 0]])
    print(result)
