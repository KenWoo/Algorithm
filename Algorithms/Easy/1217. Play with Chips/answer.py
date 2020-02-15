from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even = odd = 0
        for n in chips:
            if n % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)


if __name__ == "__main__":
    s = Solution()
    result = s.minCostToMoveChips([2, 2, 2, 3, 3])
    print(result)
