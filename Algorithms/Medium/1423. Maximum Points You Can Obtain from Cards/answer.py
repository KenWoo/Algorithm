from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        s = 0
        for i in range(N-k):
            s += cardPoints[i]
        res = s
        for i in range(k):
            j = N-k+i
            s = s - cardPoints[i] + cardPoints[j]
            res = min(res, s)
        return sum(cardPoints) - res


if __name__ == "__main__":
    s = Solution()
    result = s.maxScore([1, 2, 3, 4, 5, 6, 1], 3)
    print(result)
