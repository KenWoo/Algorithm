from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        res = 1
        anchor = 0
        N = len(A)
        for i in range(1, N):
            c = 0 if A[i-1] == A[i] else 1 if A[i-1] > A[i] else -1
            if c == 0:
                anchor = i
            elif i == N-1 or c * (0 if A[i] == A[i+1] else 1 if A[i] > A[i+1] else -1) != -1:
                res = max(res, i-anchor+1)
                anchor = i
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9])
    print(result)
