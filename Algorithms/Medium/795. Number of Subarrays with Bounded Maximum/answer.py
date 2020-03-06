from typing import List


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        res, l, r = 0, -1, -1
        for i in range(len(A)):
            if A[i] > R:
                l = r = i
                continue

            if A[i] >= L:
                r = i
            res += r - l
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3)
    print(result)
