from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        N = len(matrix[0])
        height = [0] * N

        def maxRectangleArea(hi):
            ans = 0
            s = []
            hi.append(0)
            for i in range(len(hi)):
                cur = hi[i]
                while s and cur < hi[s[-1]]:
                    w = hi[s.pop()]
                    h = i if not s else i - s[-1] - 1
                    ans = max(ans, w * h)
                s.append(i)
            return ans

        res = 0
        for row in matrix:
            for i in range(N):
                if row[i] == '0':
                    height[i] = 0
                else:
                    height[i] += 1
            res = max(res, maxRectangleArea(height))
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maximalRectangle([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ])
    print(result)
