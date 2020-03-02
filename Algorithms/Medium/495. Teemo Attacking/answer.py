from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        N, res = len(timeSeries), 0
        for i in range(N-1):
            res += min(timeSeries[i+1] - timeSeries[i], duration)
        return res + duration


if __name__ == "__main__":
    s = Solution()
    result = s.findPoisonedDuration([1, 2], 2)
    print(result)
