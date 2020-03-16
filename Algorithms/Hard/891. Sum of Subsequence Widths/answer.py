from typing import List


class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        A.sort()
        N = len(A)
        res, p = 0, 1
        for i in range(N):
            res = (res + (A[i] - A[N-i-1]) * p) % mod
            p = (p << 1) % mod
        return (res + mod) % mod


if __name__ == "__main__":
    s = Solution()
    result = s.sumSubseqWidths([2, 1, 3])
    print(result)
