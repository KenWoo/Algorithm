from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        dict = {}
        for i in range(1, N+1):
            dict[i] = {}
        for start, end in paths:
            dict[start][end] = 1
            dict[end][start] = 1
        res = [0] * N
        for i in range(N):
            colors = {1, 2, 3, 4} - {res[n-1] for n in dict[i+1]}
            res[i] = colors.pop()
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]])
    print(result)
