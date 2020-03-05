from typing import List


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.isIdealPermutation([3, 2, 1])
    print(result)
