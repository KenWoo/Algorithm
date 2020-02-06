from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f, s = cost[0], cost[1]
        for i in range(2, len(cost)):
            f, s = s, min(f, s) + cost[i]
        return min(f, s)


if __name__ == "__main__":
    s = Solution()
    result = s.minCostClimbingStairs([10, 15, 20])
    print(result)
