from typing import List


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        N = len(A)
        l = [None] * N
        r = [None] * N
        left = A[0]
        for i in range(N):
            left = max(left, A[i])
            l[i] = left
        right = A[-1]
        for i in range(N-1, -1, -1):
            right = min(right, A[i])
            r[i] = right
        for i in range(1, N):
            if l[i-1] <= r[i]:
                return i


if __name__ == "__main__":
    s = Solution()
    result = s.partitionDisjoint([5, 0, 3, 8, 6])
    print(result)
