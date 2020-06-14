from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        N = len(prices)
        for i in range(N-1):
            j = i + 1
            while j < N and prices[i] < prices[j]:
                j += 1
            res.append(prices[i] - (0 if j == N else prices[j]))
        res.append(prices[-1])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.finalPrices([8, 4, 6, 2, 3])
    print(result)
