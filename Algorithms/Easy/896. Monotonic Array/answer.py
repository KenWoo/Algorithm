from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True

        i = 0
        j = 1
        flag = 0
        while j < len(A):
            if flag == 0:
                flag = 0 if A[i] == A[j] else 1 if A[i] > A[j] else -1
            if flag > 0:
                if A[i] < A[j]:
                    return False
            elif flag < 0:
                if A[i] > A[j]:
                    return False
            i = j
            j += 1
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.isMonotonic([2, 2, 2, 1, 4, 5])
    print(result)
