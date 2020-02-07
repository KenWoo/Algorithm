from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        R = len(A)
        C = len(A[0])
        for r in range(R):
            for c in range((C + 1) // 2):
                A[r][c], A[r][C-c-1] = A[r][C-c-1] ^ 1, A[r][c] ^ 1
        return A


if __name__ == "__main__":
    s = Solution()
    result = s.flipAndInvertImage(
        [[1, 1, 0], [1, 0, 1], [0, 0, 0]])
    print(result)
