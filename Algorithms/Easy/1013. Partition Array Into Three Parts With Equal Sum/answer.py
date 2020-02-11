from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        m = sum(A)
        if m % 3 != 0:
            return False
        t = m // 3
        N = len(A)
        s = 0
        count = 0
        for n in A:
            if s != t:
                s += n
            if s == t:
                s = 0
                count += 1
        return count == 3


if __name__ == "__main__":
    s = Solution()
    result = s.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])
    print(result)
