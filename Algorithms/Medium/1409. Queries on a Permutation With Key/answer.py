from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        N = len(queries)
        P = list(range(1, m+1))
        res = [None] * N
        for i in range(N):
            q = queries[i]
            idx = P.index(q)
            res[i] = idx
            P = [P[idx]] + P[:idx] + P[idx+1:]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.processQueries([7, 5, 5, 8, 3], 8)
    print(result)
