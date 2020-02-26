from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return triangle
        N = len(triangle)
        res = []
        for n in triangle[N-1]:
            res.append(n)
        for i in range(N-2, -1, -1):
            for j in range(i+1):
                res[j] = triangle[i][j] + min(res[j], res[j+1])
        return res[0]


if __name__ == "__main__":
    s = Solution()
    result = s.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ])
    print(result)
