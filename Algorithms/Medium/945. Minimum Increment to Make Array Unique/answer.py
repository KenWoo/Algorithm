from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        N = len(A)
        res = 0
        for i in range(1, N):
            if A[i] <= A[i-1]:
                tmp = A[i]
                A[i] = A[i-1] + 1
                res += A[i]-tmp
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.minIncrementForUnique([3, 2, 1, 2, 1, 7])
    print(result)
