from typing import List


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        else:
            return 0.5


if __name__ == "__main__":
    s = Solution()
    result = s.nthPersonGetsNthSeat(1)
    print(result)
