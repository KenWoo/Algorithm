from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i <= num // i:
            if i * i == num:
                return True
            i += 1
        return False


if __name__ == "__main__":
    s = Solution()
    result = s.isPerfectSquare(16)
    print(result)
