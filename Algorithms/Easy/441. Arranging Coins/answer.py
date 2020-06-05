from typing import List


class Solution:
    def arrangeCoins(self, n: int) -> int:
        s = count = 0
        for i in range(1, n+1):
            s += i
            count += 1
            if s + i + 1 > n:
                break
        return count


if __name__ == "__main__":
    s = Solution()
    result = s.arrangeCoins(1)
    print(result)
