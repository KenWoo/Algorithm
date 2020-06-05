from typing import List


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and (num & (num-1)) == 0 and (num-1) % 3 == 0


if __name__ == "__main__":
    s = Solution()
    result = s.isPowerOfFour(15)
    print(result)
