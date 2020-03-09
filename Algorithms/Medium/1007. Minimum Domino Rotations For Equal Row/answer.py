from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if len(A) != len(B):
            return -1
        N = len(A)
        a = b = i = 0
        while i < N and (A[i] == A[0] or B[i] == A[0]):
            if A[i] != A[0]:
                a += 1
            if B[i] != A[0]:
                b += 1
            if i == N-1:
                return min(a, b)
            i += 1
        a = b = i = 0
        while i < N and (A[i] == B[0] or B[i] == B[0]):
            if A[i] != B[0]:
                a += 1
            if B[i] != B[0]:
                b += 1
            if i == N-1:
                return min(a, b)
            i += 1
        return -1


if __name__ == "__main__":
    s = Solution()
    A = [2]
    B = [5]
    result = s.minDominoRotations(A, B)
    print(result)
