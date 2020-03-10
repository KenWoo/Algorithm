from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N = len(A)
        presum = [0]*(N+1)
        for i in range(N):
            presum[i+1] = A[i] + presum[i]

        def maxsum(start, end):
            res = -1
            for j in range(start, end+1):
                res = max(res, presum[j+M]-presum[j])
            return res
        ans = -1
        for i in range(N-L+1):
            ls = presum[i+L] - presum[i]
            ms = max(maxsum(0, i-M-1), maxsum(i+L, N-M))
            ans = max(ans, ls + ms)
        return ans


if __name__ == "__main__":
    s = Solution()
    result = s.maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2)
    print(result)
