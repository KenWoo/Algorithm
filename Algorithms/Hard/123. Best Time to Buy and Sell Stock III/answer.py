from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1 = b2 = float('-inf')
        s1 = s2 = 0
        for p in prices:
            b1 = max(b1, -p)
            s1 = max(s1, b1 + p)
            b2 = max(b2, s1 - p)
            s2 = max(s2, b2 + p)
        return s2


if __name__ == "__main__":
    s = Solution()
    result = s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
    print(result)
