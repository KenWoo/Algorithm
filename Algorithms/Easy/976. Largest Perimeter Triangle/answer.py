from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A)-3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0


if __name__ == "__main__":
    s = Solution()
    result = s.largestPerimeter([2, 1, 2])
    print(result)
