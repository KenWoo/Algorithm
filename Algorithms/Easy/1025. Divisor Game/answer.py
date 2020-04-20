from typing import List


class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


if __name__ == "__main__":
    s = Solution()
    result = s.divisorGame(3)
    print(result)
