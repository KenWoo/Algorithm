from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        N = len(points)
        res = 0
        for i in range(N):
            dict = {}
            for j in range(N):
                if i == j:
                    continue
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                d = x * x + y * y
                dict.setdefault(d, 0)
                dict[d] += 1
            for v in dict.values():
                res += v * (v - 1)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])
    print(result)
