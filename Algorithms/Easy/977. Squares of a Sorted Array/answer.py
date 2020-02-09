from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        N = len(A)
        pivot = 0
        for i in range(len(A)):
            if A[i] >= 0:
                pivot = i
                break

        i = pivot - 1
        j = pivot
        l = []
        while i >= 0 and j <= N-1:
            if A[i]**2 < A[j]**2:
                l.append(A[i]**2)
                i -= 1
            else:
                l.append(A[j]**2)
                j += 1
        while i >= 0:
            l.append(A[i]**2)
            i -= 1
        while j <= N-1:
            l.append(A[j]**2)
            j += 1
        return l


if __name__ == "__main__":
    s = Solution()
    result = s.sortedSquares([-4, -1, 0, 3, 10])
    print(result)
