from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) < 2:
            return 0
        max = 0
        min = prices[0]
        for p in prices:
            if p < min:
                min = p
            else:
                if max < p - min:
                    max = p - min

        return max


if __name__ == "__main__":
    s = Solution()
    result = s.maxProfit([7, 1, 5, 3, 6, 4])
    print(result)
