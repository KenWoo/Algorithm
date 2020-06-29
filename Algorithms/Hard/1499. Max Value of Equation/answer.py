from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = float('-inf')
        q = []
        for j in range(len(points)):
            xj = points[j][0]
            yj = points[j][1]
            while q and xj - points[q[0]][0] > k:
                q.pop(0)
            if q:
                i = q[0]
                xi = points[i][0]
                yi = points[i][1]
                res = max(res, xj - xi + yi + yj)
            while q and yj - xj >= points[q[-1]][1] - points[q[-1]][0]:
                q.pop()
            q.append(j)
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.findMaxValueOfEquation([[0,0],[3,0],[9,2]], 3)
    print(result)