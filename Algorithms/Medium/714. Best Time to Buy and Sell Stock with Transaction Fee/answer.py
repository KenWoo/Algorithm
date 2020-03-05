from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash


if __name__ == "__main__":
    s = Solution()
    result = s.maxProfit([1, 3, 2, 8, 4, 9], 2)
    print(result)
