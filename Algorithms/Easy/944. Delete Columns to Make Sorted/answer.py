from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        for j in range(len(A[0])):
            for i in range(len(A)-1):
                if A[i][j] > A[i+1][j]:
                    res += 1
                    break
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.minDeletionSize(["cba", "daf", "ghi"])
    print(result)
