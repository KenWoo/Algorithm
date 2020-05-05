from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        N = len(points)
        res = 0
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    area = .5 * \
                        abs(points[i][0]*(points[j][1]-points[k][1]) +
                            points[j][0]*(points[k][1]-points[i][1]) +
                            points[k][0]*(points[i][1]-points[j][1]))
                    res = max(res, area)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]])
    print(result)
