from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while i * i <= x:
            i += 1
        return i - 1


if __name__ == "__main__":
    s = Solution()
    result = s.mySqrt(9)
    print(result)
