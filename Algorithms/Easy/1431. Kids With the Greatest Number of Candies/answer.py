from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ma = max(candies)
        res = []
        for c in candies:
            if c + extraCandies >= ma:
                res.append(True)
            else:
                res.append(False)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.kidsWithCandies([2, 3, 5, 1, 3], 3)
    print(result)
