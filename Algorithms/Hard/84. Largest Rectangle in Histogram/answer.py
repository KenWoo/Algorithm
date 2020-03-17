from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        heights.append(0)
        N = len(heights)
        res = 0
        for i in range(N):
            if not s or heights[i] > heights[s[-1]]:
                s.append(i)
            else:
                while s and heights[i] <= heights[s[-1]]:
                    h = heights[s[-1]]
                    s.pop()
                    w = i if not s else i - s[-1] - 1
                    res = max(res, w * h)
                s.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.largestRectangleArea([2, 1, 5, 6, 2, 3])
    print(result)
