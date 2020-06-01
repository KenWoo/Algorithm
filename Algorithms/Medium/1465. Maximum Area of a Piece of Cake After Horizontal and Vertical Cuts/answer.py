from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        maxH = 0
        for i in range(len(horizontalCuts)-1):
            maxH = max(maxH, horizontalCuts[i+1]-horizontalCuts[i])
        maxW = 0
        for i in range(len(verticalCuts)-1):
            maxW = max(maxW, verticalCuts[i+1]-verticalCuts[i])
        return maxH * maxW % 1000000007


if __name__ == "__main__":
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]
    s = Solution()
    result = s.maxArea(h, w, horizontalCuts, verticalCuts)
    print(result)
