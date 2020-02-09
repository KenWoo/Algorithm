from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        N = len(A)
        if N < 3:
            return False

        point = 0
        for i in range(1, N - 1):
            if A[i] > A[point]:
                point = i
            elif A[i] == A[point]:
                return False
            else:
                break

        if point == 0:
            return False

        for i in range(point + 1, N):
            if A[i] >= A[point]:
                return False
            else:
                point = i

        return True


if __name__ == "__main__":
    s = Solution()
    result = s.validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    print(result)
