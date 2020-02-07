from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        R = len(A)
        C = len(A[0])
        l = []
        for j in range(C):
            r = []
            for i in range(R):
                r.append(A[i][j])
            l.append(r)
        return l


if __name__ == "__main__":
    s = Solution()
    result = s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(result)
