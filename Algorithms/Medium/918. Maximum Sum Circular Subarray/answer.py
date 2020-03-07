from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(list):
            res = cur = float('-inf')
            for x in list:
                cur = x + max(cur, 0)
                res = max(res, cur)
            return res

        N = len(A)
        S = sum(A)
        res1 = kadane(A)
        res2 = S + kadane([-A[i] for i in range(1, N)])
        res3 = S + kadane([-A[i] for i in range(N-1)])
        return max(res1, res2, res3)


if __name__ == "__main__":
    s = Solution()
    result = s.maxSubarraySumCircular([-2, -3, -1])
    print(result)
