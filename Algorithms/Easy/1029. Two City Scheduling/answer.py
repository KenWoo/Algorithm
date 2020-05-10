from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        N = len(costs)
        res = 0
        for c in costs[0:N//2]:
            res += c[0]
        for c in costs[N//2:]:
            res += c[1]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.twoCitySchedCost([[259, 770], [448, 54], [926, 667], [
                                184, 139], [840, 118], [577, 469]])
    print(result)
