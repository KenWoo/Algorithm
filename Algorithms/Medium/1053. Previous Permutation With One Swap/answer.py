from typing import List


class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        N = len(A)
        i = N - 1
        while i > 0 and A[i-1] <= A[i]:
            i -= 1
        if i == 0:
            return A
        i -= 1
        j = N - 1
        while A[j] >= A[i] or j > 0 and A[j] == A[j-1]:
            print(A[j], A[i])
            j -= 1
        A[i], A[j] = A[j], A[i]
        return A


if __name__ == "__main__":
    s = Solution()
    result = s.prevPermOpt1([3, 1, 1, 3])
    print(result)
