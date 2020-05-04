from typing import List


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]
        N = len(b)
        if N < 2:
            return True
        for i in range(N-1):
            if b[i] == b[i+1]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.hasAlternatingBits(11)
    print(result)
