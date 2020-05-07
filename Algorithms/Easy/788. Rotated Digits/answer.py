from typing import List


class Solution:
    def rotatedDigits(self, N: int) -> int:
        res = 0
        for i in range(1, N+1):
            S = str(i)
            if '3' in S or '7' in S or '4' in S:
                continue
            if '2' in S or '5' in S or '6' in S or '9' in S:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.rotatedDigits(857)
    print(result)
