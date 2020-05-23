from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        l = [0] * (N + 1)
        for t in trust:
            l[t[0]] -= 1
            l[t[1]] += 1
        for i in range(1, N+1):
            if l[i] == N - 1:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    result = s.findJudge(3, [[1, 3], [2, 3]])
    print(result)
